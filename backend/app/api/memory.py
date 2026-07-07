from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.memory import MemoryCreate
from app.services.memory_service import MemoryService
from app.services.twin_update_service import TwinUpdateService

router = APIRouter(
    prefix="/memory",
    tags=["Memory"],
)

memory_service = MemoryService()
twin_service = TwinUpdateService()


@router.post("/")
def create_memory(
    memory: MemoryCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    memory_service.remember(
        db=db,
        user_id=current_user.id,
        title=memory.title,
        description=memory.description,
    )


    return memory

@router.get("/latest-analysis")
def latest_analysis(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    analysis = memory_service.analysis_repository.latest_by_user(
        db=db,
        user_id=current_user.id,
    )

    return analysis

@router.get("/")
def get_memories(

    current_user: User = Depends(get_current_user),

    db: Session = Depends(get_db),

):

    return memory_service.get_all(

        db=db,

        user_id=current_user.id,

    )