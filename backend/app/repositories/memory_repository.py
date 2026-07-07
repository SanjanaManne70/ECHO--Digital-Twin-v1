from sqlalchemy import Date
from sqlalchemy.orm import Session

from app.models.memory_event import MemoryEvent


class MemoryRepository:

    def create(
        self,
        db: Session,
        memory: MemoryEvent,
    ):
        db.add(memory)
        db.commit()
        db.refresh(memory)

        return memory

    def get_by_user(
        self,
        db: Session,
        user_id: int,
    ):
        return (
            db.query(MemoryEvent)
            .filter(
                MemoryEvent.user_id == user_id
            )
            .order_by(
                MemoryEvent.created_at.desc()
            )
            .all()
        )
    
    def latest_memories(
        self,
        db,
        user_id,
        limit=5,
    ):

        return (
            db.query(MemoryEvent)
            .filter(
                MemoryEvent.user_id == user_id,
            )
            .order_by(
                MemoryEvent.created_at.desc(),
            )
            .limit(limit)
            .all()
        )
    
    def get_recent(
        self,
        db,
        user_id,
        limit=10,
    ):

        return (
            db.query(MemoryEvent)
            .filter(
                MemoryEvent.user_id == user_id
            )
            .order_by(
                MemoryEvent.created_at.desc()
            )
            .limit(limit)
            .all()
        )
    
    def get_by_id(
        self,
        db,
        memory_id,
    ):
        return (
            db.query(MemoryEvent)
            .filter(
                MemoryEvent.id == memory_id,
            )
            .first()
        )
    
    def get_all(
        self,
        db,
        user_id,
    ):

        return (
            db.query(MemoryEvent)
            .filter(
                MemoryEvent.user_id == user_id,
            )
            .order_by(
                MemoryEvent.created_at.desc(),
            )
            .all()
        )
    
    def get_by_day(
        self,
        db,
        user_id,
        day,
    ):

        return (

            db.query(MemoryEvent)

            .filter(

                MemoryEvent.user_id == user_id,

                MemoryEvent.created_at.cast(Date) == day,

            )

            .all()

        )