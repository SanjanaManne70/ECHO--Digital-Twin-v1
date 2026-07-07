from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Float,
    ForeignKey,
    DateTime,
)

from sqlalchemy.sql import func

from app.database.base import Base


class Goal(Base):

    __tablename__ = "goals"

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

    title = Column(
        String,
        nullable=False,
    )

    category = Column(
        String,
        nullable=False,
    )

    target_value = Column(
        Float,
        nullable=False,
    )

    target_unit = Column(
        String,
        nullable=False,
    )

    current_value = Column(
        Float,
        default=0,
    )

    progress = Column(
        Float,
        default=0,
    )

    description = Column(
        String,
        default="",
    )

    ai_reason = Column(
        String,
        default="Goal created.",
    )

    predicted_completion = Column(
        String,
        default="Calculating...",
    )

    completed = Column(
        Boolean,
        default=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )