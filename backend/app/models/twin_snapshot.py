from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey,
)

from sqlalchemy.sql import func

from app.database import Base


class TwinSnapshot(Base):

    __tablename__ = "twin_snapshots"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    sleep = Column(Float, nullable=False)

    energy = Column(Float, nullable=False)

    mood = Column(Float, nullable=False)

    learning = Column(Float, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )