from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user

from app.ai.trend_analyzer import TrendAnalyzer

from app.repositories.twin_snapshot_repository import (
    TwinSnapshotRepository,
)

router = APIRouter(
    prefix="/trend",
    tags=["Trend"],
)

repo = TwinSnapshotRepository()

analyzer = TrendAnalyzer()


@router.get("/")
def get_trend(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user),

):

    snapshots = repo.get_history(

        db,

        current_user.id,

    )

    return analyzer.analyze(

        snapshots,

    )