from sqlalchemy import Column, Integer, ForeignKey, Text, Date, Boolean
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from app.database.base import Base


class Reflection(Base):

    __tablename__ = "reflections"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    date = Column(
        Date,
        nullable=False,
    )

    content = Column(
        Text,
        nullable=False,
    )

    needs_refresh = Column(
        Boolean,
        default=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )