from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.services.timeline_service import TimelineService

router = APIRouter(
    prefix="/timeline",
    tags=["Timeline"],
)

service = TimelineService()


@router.get("/")
def get_timeline(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return service.get_timeline(
        db=db,
        user_id=current_user.id,
    )