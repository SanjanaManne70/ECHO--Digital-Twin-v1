from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db,
    get_current_user,
)

from app.models.user import User

from app.schemas.goal import GoalCreate

from app.services.goal_service import GoalService

router = APIRouter(
    prefix="/goal",
    tags=["Goal"],
)

service = GoalService()


@router.get("/")
def get_goals(

    current_user: User = Depends(get_current_user),

    db: Session = Depends(get_db),

):

    return service.get_all(

        db=db,

        user_id=current_user.id,

    )


@router.post("/")
def create_goal(

    goal: GoalCreate,

    current_user: User = Depends(get_current_user),

    db: Session = Depends(get_db),

):

    return service.create(
    db=db,
    user_id=current_user.id,
    title=goal.title,
    description=goal.description,
)

@router.delete("/{goal_id}")
def delete_goal(

    goal_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):

    return service.delete(

        db=db,

        goal_id=goal_id,

    )