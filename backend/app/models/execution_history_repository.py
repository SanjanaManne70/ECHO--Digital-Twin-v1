
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy.orm import Session

from app.models.workflow_run import WorkflowRun
from app.models.agent_execution_record import AgentExecutionRecord


class ExecutionHistoryRepository:
    """Persist coordinator workflow traces without storing raw prompts or memories."""

    def persist_trace(
        self,
        db: Session,
        context,
        trace,
        started_at: datetime,
        workflow_name: str = "custom_workflow",
    ) -> WorkflowRun:
        """Save one workflow run and its agent records atomically."""

        user_id: Optional[int] = getattr(context, "user_id", None)

        if user_id is None:
            user = getattr(context, "user", None)
            user_id = getattr(user, "id", None)

        workflow_run = WorkflowRun(
            user_id=user_id,
            workflow_name=workflow_name,
            status=trace.workflow_status,
            success=trace.success,
            started_at=started_at,
            finished_at=datetime.now(timezone.utc),
            total_duration_ms=trace.total_duration_ms,
            agent_execution_duration_ms=(
                trace.agent_execution_duration_ms
            ),
            abort_reason=trace.abort_reason,
        )

        try:
            db.add(workflow_run)
            db.flush()

            for execution in trace.executions:
                # Never persist arbitrary exception strings from agent results.
                if execution.success:
                    error_summary = None
                elif execution.skipped:
                    error_summary = (
                        "Agent skipped because a dependency failed."
                    )
                elif execution.not_run:
                    error_summary = (
                        "Agent was not run because the workflow was aborted."
                    )
                else:
                    error_summary = "Agent execution failed."

                record = AgentExecutionRecord(
                    workflow_run_id=workflow_run.id,
                    agent_name=execution.agent_name,
                    status=execution.status,
                    success=execution.success,
                    duration_ms=execution.duration_ms,
                    error_summary=error_summary,
                )
                db.add(record)

            db.commit()
            db.refresh(workflow_run)

            return workflow_run

        except Exception:
            db.rollback()
            raise
