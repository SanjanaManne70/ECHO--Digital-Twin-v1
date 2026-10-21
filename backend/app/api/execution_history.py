
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.models.workflow_run import WorkflowRun
from app.models.agent_execution_record import AgentExecutionRecord

router = APIRouter(
    prefix="/execution-history",
    tags=["Execution History"],
)


def serialize_workflow_run(run: WorkflowRun) -> dict:
    return {
        "id": run.id,
        "workflow_name": run.workflow_name,
        "status": run.status,
        "success": run.success,
        "started_at": run.started_at,
        "finished_at": run.finished_at,
        "total_duration_ms": run.total_duration_ms,
        "agent_execution_duration_ms": run.agent_execution_duration_ms,
        "abort_reason": run.abort_reason,
        "created_at": run.created_at,
    }


def serialize_agent_execution(
    record: AgentExecutionRecord,
) -> dict:
    return {
        "id": record.id,
        "agent_name": record.agent_name,
        "status": record.status,
        "success": record.success,
        "duration_ms": record.duration_ms,
        "error_summary": record.error_summary,
        "created_at": record.created_at,
    }


@router.get("/")
def list_execution_history(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    query = db.query(WorkflowRun).filter(
        WorkflowRun.user_id == current_user.id
    )

    total = query.count()

    runs = (
        query.order_by(
            WorkflowRun.started_at.desc(),
            WorkflowRun.id.desc(),
        )
        .offset(offset)
        .limit(limit)
        .all()
    )

    return {
        "items": [serialize_workflow_run(run) for run in runs],
        "total": total,
        "limit": limit,
        "offset": offset,
    }


@router.get("/{run_id}")
def get_execution_history_detail(
    run_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    run = (
        db.query(WorkflowRun)
        .filter(
            WorkflowRun.id == run_id,
            WorkflowRun.user_id == current_user.id,
        )
        .first()
    )

    if run is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow run not found",
        )

    records = (
        db.query(AgentExecutionRecord)
        .filter(
            AgentExecutionRecord.workflow_run_id == run.id
        )
        .order_by(AgentExecutionRecord.id.asc())
        .all()
    )

    result = serialize_workflow_run(run)
    result["agent_executions"] = [
        serialize_agent_execution(record)
        for record in records
    ]

    return result
