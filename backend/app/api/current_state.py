from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.repositories.current_state_repository import CurrentStateRepository

router = APIRouter(
    prefix="/current-state",
    tags=["Current State"],
)

repository = CurrentStateRepository()


@router.get("/")
def get_current_state(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    states = repository.get_by_user(
        db,
        current_user.id,
    )

    return {
        state.domain: state.value
        for state in states
    }