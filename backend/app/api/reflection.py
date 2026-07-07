from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import ( get_db, get_current_user )

from app.services.reflection_service import (
    ReflectionService,
)

router = APIRouter(
    prefix="/reflection",
    tags=["Reflection"],
)

service = ReflectionService()


@router.get("/")
def get_reflection(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):

    return {

        "reflection": service.reflect(

            db,

            current_user.id,

        )

    }