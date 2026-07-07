from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.services.planner_service import PlannerService

router = APIRouter(
    prefix="/planner",
    tags=["Planner"],
)

service = PlannerService()


@router.get("/")
def pending_tasks(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):

    return service.repository.get_pending(

        db=db,

        user_id=current_user.id,

    )


@router.get("/completed")
def completed_tasks(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):

    return service.get_completed(

        db=db,

        user_id=current_user.id,

    )


@router.post("/")
def create_task(

    body: dict,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):

    return service.create_manual_task(

        db=db,

        user_id=current_user.id,

        title=body["title"],

    )


@router.put("/{task_id}")
def complete_task(

    task_id: int,

    db: Session = Depends(get_db),

):

    return service.complete_task(

        db=db,

        task_id=task_id,

    )
@router.delete("/completed")
def delete_completed(

    db: Session = Depends(get_db),

    current_user = Depends(get_current_user),

):

    service.clear_completed(

        db,

        current_user.id,

    )

    return {

        "message":"Deleted"

    }
