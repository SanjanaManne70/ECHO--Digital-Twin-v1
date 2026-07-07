from fastapi import APIRouter
from sqlalchemy import text

from app.database.session import SessionLocal

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/db")
def database_health():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))

        return {
            "database": "connected",
        }

    finally:
        db.close()
