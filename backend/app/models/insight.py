from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class Insight(Base):

    __tablename__ = "insights"

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

    description = Column(
        String,
        nullable=False,
    )

    severity = Column(
        String,
        nullable=False,
    )

    is_read = Column(
        Boolean,
        default=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )