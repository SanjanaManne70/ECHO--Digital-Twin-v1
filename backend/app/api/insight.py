from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.repositories.insight_repository import InsightRepository

router = APIRouter(
    prefix="/insight",
    tags=["Insight"],
)

repository = InsightRepository()


@router.get("/")
def latest_insight(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return repository.latest_by_user(
        db=db,
        user_id=current_user.id,
    )