
from datetime import datetime, timezone
from typing import Callable, Optional

from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.models.workflow_run import WorkflowRun
from app.models.agent_execution_record import AgentExecutionRecord


class ExecutionHistoryRepository:
    """Persist safe workflow traces in an isolated database session."""

    def __init__(
        self,
        session_factory: Callable[[], Session] = SessionLocal,
    ):
        self.session_factory = session_factory

    def persist_trace(
        self,
        context,
        trace,
        started_at: datetime,
        workflow_name: str = "custom_workflow",
    ) -> WorkflowRun:
        user_id = getattr(context, "user_id", None)
        print(
            f"[EXECUTION HISTORY DEBUG] "
            f"context_type={type(context).__name__}, "
            f"user_id={user_id}, "
            f"workflow_name={workflow_name}"
        )
        if user_id is None:
            user = getattr(context, "user", None)
            user_id = getattr(user, "id", None)

        db = self.session_factory()

        try:
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

            db.add(workflow_run)
            db.flush()

            for execution in trace.executions:
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

                db.add(
                    AgentExecutionRecord(
                        workflow_run_id=workflow_run.id,
                        agent_name=execution.agent_name,
                        status=execution.status,
                        success=execution.success,
                        duration_ms=execution.duration_ms,
                        error_summary=error_summary,
                    )
                )

            db.commit()
            db.refresh(workflow_run)
            return workflow_run

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()



