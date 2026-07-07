from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    DateTime,
)

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from app.database.base import Base

from sqlalchemy import Boolean
class DailyChapter(Base):

    __tablename__ = "daily_chapters"

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

    date = Column(
        Date,
        nullable=False,
    )

    title = Column(
        String,
        nullable=False,
    )

    mood = Column(
        String,
        nullable=False,
    )

    summary = Column(
        String,
        nullable=False,
    )

    growth = Column(
        JSONB,
        nullable=False,
    )

    highlight = Column(
        String,
        nullable=False,
    )

    tomorrow_focus = Column(
        String,
        nullable=False,
    )
    needs_refresh = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
