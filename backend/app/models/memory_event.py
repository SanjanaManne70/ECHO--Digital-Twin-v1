from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.sql import func

from app.database.base import Base


class MemoryEvent(Base):
    __tablename__ = "memory_events"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    title = Column(
        String,
        nullable=False,
    )

    description = Column(
        Text,
        nullable=False,
    )

  

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )