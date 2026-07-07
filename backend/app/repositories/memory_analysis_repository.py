from sqlalchemy.orm import Session

from app.models.memory_analysis import MemoryAnalysis
from app.models.memory_event import MemoryEvent


class MemoryAnalysisRepository:

    def create(
        self,
        db: Session,
        analysis: MemoryAnalysis,
    ):
        db.add(analysis)
        db.commit()
        db.refresh(analysis)

        return analysis

    def latest_by_user(
        self,
        db: Session,
        user_id: int,
    ):

        return (
            db.query(MemoryAnalysis)
            .join(
                MemoryEvent,
                MemoryAnalysis.memory_id == MemoryEvent.id,
            )
            .filter(
                MemoryEvent.user_id == user_id,
            )
            .order_by(
                MemoryAnalysis.id.desc(),
            )
            .first()
        )

    def get_recent(
        self,
        db: Session,
        user_id: int,
        limit: int = 30,
    ):

        return (
            db.query(MemoryAnalysis)
            .join(
                MemoryEvent,
                MemoryAnalysis.memory_id == MemoryEvent.id,
            )
            .filter(
                MemoryEvent.user_id == user_id,
            )
            .order_by(
                MemoryAnalysis.id.desc(),
            )
            .limit(limit)
            .all()
        )