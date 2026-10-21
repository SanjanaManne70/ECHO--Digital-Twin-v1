
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentExecution:
    """Execution details for one agent."""

    agent_name: str
    success: bool
    duration_ms: float
    error: Optional[str] = None
    skipped: bool = False
    not_run: bool = False

    @property
    def status(self) -> str:
        """Return a readable execution status."""
        if self.not_run:
            return "not_run"
        if self.skipped:
            return "skipped"
        if self.success:
            return "succeeded"
        return "failed"

    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON-serializable representation."""
        data = asdict(self)
        data["status"] = self.status
        return data


@dataclass
class ExecutionTrace:
    """Execution history and outcome for an agent workflow."""

    executions: List[AgentExecution] = field(default_factory=list)
    total_duration_ms: float = 0.0
    workflow_status: str = "completed"
    abort_reason: Optional[str] = None
    agent_execution_duration_ms: float = 0.0

    def add(self, execution: AgentExecution) -> None:
        """Record an agent execution and accumulate its duration."""
        self.executions.append(execution)

        if not execution.not_run and not execution.skipped:
            self.agent_execution_duration_ms += execution.duration_ms

    def get(self, agent_name: str) -> Optional[AgentExecution]:
        """Find an execution by agent name."""
        for execution in self.executions:
            if execution.agent_name == agent_name:
                return execution
        return None

    @property
    def success(self) -> bool:
        """Return True only if the workflow completed successfully."""
        if self.workflow_status == "aborted":
            return False

        executed = [
            execution
            for execution in self.executions
            if not execution.skipped and not execution.not_run
        ]

        return bool(executed) and all(
            execution.success for execution in executed
        )

    def to_dict(self) -> Dict[str, Any]:
        """Return the complete trace in a JSON-serializable format."""
        return {
            "success": self.success,
            "workflow_status": self.workflow_status,
            "abort_reason": self.abort_reason,
            "total_duration_ms": round(self.total_duration_ms, 3),
            "agent_execution_duration_ms": round(
                self.agent_execution_duration_ms, 3
            ),
            "agent_count": len(self.executions),
            "executions": [
                execution.to_dict()
                for execution in self.executions
            ],
        }
