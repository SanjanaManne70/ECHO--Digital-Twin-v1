from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
)

from app.database.base import Base


class MemoryAnalysis(Base):

    __tablename__ = "memory_analysis"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    memory_id = Column(
        Integer,
        ForeignKey("memory_events.id"),
    )

    sentiment = Column(String)

    emotion = Column(String)

    confidence = Column(Float)

    severity = Column(String)

    reason = Column(String)