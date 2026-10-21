
import logging
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Union

from app.repositories.execution_history_repository import (
    ExecutionHistoryRepository,
)

from .agent_context_loader import AgentContextLoader
from .context import AgentContext
from .execution import AgentExecution, ExecutionTrace
from .registry import AgentRegistry
from .result import AgentResult
from .workflow import AgentStep


logger = logging.getLogger(__name__)


class Coordinator:
    """
    Central orchestration layer for ECHO V2.

    Validates workflows, executes agents, manages dependencies,
    refreshes shared context, and records execution traces.
    """

    def __init__(
        self,
        registry: AgentRegistry,
        context_loader: Optional[AgentContextLoader] = None,
        execution_history_repository: Optional[
            ExecutionHistoryRepository
        ] = None,
    ):
        self.registry = registry
        self.context_loader = context_loader or AgentContextLoader()
        self.execution_history_repository = (
            execution_history_repository
            if execution_history_repository is not None
            else ExecutionHistoryRepository()
        )

    def _validate_workflow(
        self,
        workflow: List[Union[str, AgentStep]],
    ) -> List[AgentStep]:
        """Normalize and validate agents and dependency ordering."""

        normalized_workflow: List[AgentStep] = []
        seen_agents = set()

        for item in workflow:
            if isinstance(item, str):
                step = AgentStep(agent_name=item)
            elif isinstance(item, AgentStep):
                step = item
            else:
                raise TypeError(
                    "Workflow entries must be agent names or AgentStep "
                    f"instances; received {type(item).__name__}."
                )

            agent_name = step.agent_name

            if agent_name in seen_agents:
                raise ValueError(
                    f"Duplicate agent '{agent_name}' in workflow."
                )

            seen_agents.add(agent_name)
            self.registry.get(agent_name)
            normalized_workflow.append(step)

        available_agents = set()

        for step in normalized_workflow:
            for dependency in step.depends_on:
                if dependency not in seen_agents:
                    raise ValueError(
                        f"Agent '{step.agent_name}' depends on "
                        f"'{dependency}', which is not in the workflow."
                    )

                if dependency not in available_agents:
                    raise ValueError(
                        f"Dependency '{dependency}' for agent "
                        f"'{step.agent_name}' must appear before the agent."
                    )

            available_agents.add(step.agent_name)

        return normalized_workflow

    def run(
        self,
        context: AgentContext,
        workflow: List[Union[str, AgentStep]],
    ) -> Dict[str, AgentResult]:
        """
        Execute a workflow and return results.

        Agent failures do not stop unrelated agents. Failed dependencies
        cause dependent agents to be skipped unless explicitly allowed.
        Context refresh failures abort the remaining workflow.
        """

        workflow = self._validate_workflow(workflow)

        results: Dict[str, AgentResult] = {}
        trace = ExecutionTrace()

        workflow_started_at = datetime.now(timezone.utc)
        workflow_start = time.perf_counter()

        for index, step in enumerate(workflow):
            agent_name = step.agent_name

            dependencies_satisfied = all(
                dependency in results
                and results[dependency].success
                for dependency in step.depends_on
            )

            # Skip agents with unsatisfied dependencies.
            if (
                not dependencies_satisfied
                and not step.run_if_dependencies_failed
            ):
                error_message = (
                    f"Dependency failed for agent '{agent_name}'."
                )

                result = AgentResult(
                    success=False,
                    agent_name=agent_name,
                    message="Agent skipped because a dependency failed.",
                    errors=[error_message],
                    metadata={
                        "skipped": True,
                        "dependencies": step.depends_on,
                    },
                )

                results[agent_name] = result
                context.store_result(agent_name, result)

                trace.add(
                    AgentExecution(
                        agent_name=agent_name,
                        success=False,
                        duration_ms=0.0,
                        error=error_message,
                        skipped=True,
                    )
                )
                continue

            agent = self.registry.get(agent_name)
            agent_start = time.perf_counter()

            try:
                result = agent.run(context)

                # Enforce the common agent-result contract.
                if not isinstance(result, AgentResult):
                    raise TypeError(
                        f"Agent '{agent_name}' returned invalid result "
                        f"type '{type(result).__name__}'; "
                        "expected AgentResult."
                    )

                duration_ms = (
                    time.perf_counter() - agent_start
                ) * 1000

                trace.add(
                    AgentExecution(
                        agent_name=agent_name,
                        success=result.success,
                        duration_ms=duration_ms,
                        error=(
                            "; ".join(result.errors)
                            if not result.success and result.errors
                            else None
                        ),
                    )
                )

            except Exception as exc:
                duration_ms = (
                    time.perf_counter() - agent_start
                ) * 1000

                # Keep sensitive exception messages out of logs.
                logger.error(
                    "Agent execution failed: agent=%s, exception_type=%s",
                    agent_name,
                    type(exc).__name__,
                )

                safe_error = (
                    f"Agent '{agent_name}' failed during execution."
                )

                result = AgentResult(
                    success=False,
                    agent_name=agent_name,
                    message=(
                        f"Agent '{agent_name}' failed during execution."
                    ),
                    errors=[str(exc)],
                    metadata={
                        "exception_type": type(exc).__name__,
                    },
                )

                trace.add(
                    AgentExecution(
                        agent_name=agent_name,
                        success=False,
                        duration_ms=duration_ms,
                        error=safe_error,
                    )
                )

            # Store the result for subsequent agents.
            results[agent_name] = result
            context.store_result(agent_name, result)

            # Refresh shared context after a successful agent.
            if result.success and index < len(workflow) - 1:
                try:
                    self.context_loader.refresh(context)

                except Exception as exc:
                    abort_reason = (
                        f"Context refresh failed after agent "
                        f"'{agent_name}'."
                    )

                    logger.error(
                        "Context refresh failed: after_agent=%s, "
                        "exception_type=%s",
                        agent_name,
                        type(exc).__name__,
                    )

                    context.metadata["context_refresh_error"] = {
                        "after_agent": agent_name,
                        "error": "Context refresh failed.",
                        "exception_type": type(exc).__name__,
                    }
                    context.metadata["workflow_aborted"] = True

                    trace.workflow_status = "aborted"
                    trace.abort_reason = abort_reason

                    # Explicitly record every agent that never ran.
                    for remaining_step in workflow[index + 1:]:
                        remaining_name = remaining_step.agent_name

                        not_run_result = AgentResult(
                            success=False,
                            agent_name=remaining_name,
                            message=(
                                "Agent not run because the workflow "
                                "was aborted."
                            ),
                            errors=[abort_reason],
                            metadata={
                                "not_run": True,
                                "reason": "workflow_aborted",
                            },
                        )

                        results[remaining_name] = not_run_result
                        context.store_result(
                            remaining_name, not_run_result
                        )

                        trace.add(
                            AgentExecution(
                                agent_name=remaining_name,
                                success=False,
                                duration_ms=0.0,
                                error=abort_reason,
                                not_run=True,
                            )
                        )

                    break

        # Total wall-clock time includes orchestration and refreshes.
        trace.total_duration_ms = (
            time.perf_counter() - workflow_start
        ) * 1000

        # Distinguish completed workflows with failures from aborted ones.
        if (
            trace.workflow_status != "aborted"
            and not trace.success
        ):
            trace.workflow_status = "completed_with_failures"

        context.metadata["execution_trace"] = trace

        # Persist execution history using the repository's isolated
        # database session. Persistence failures must not interrupt
        # the agent workflow.
        if self.execution_history_repository is not None:
            try:
                self.execution_history_repository.persist_trace(
                    context=context,
                    trace=trace,
                    started_at=workflow_started_at,
                )
            except Exception as exc:
                # Do not log exception messages that could contain
                # sensitive information.
                logger.error(
                    "Execution history persistence failed: "
                    "exception_type=%s",
                    type(exc).__name__,
                )

        return results
