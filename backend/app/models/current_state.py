from sqlalchemy import Column, Float, ForeignKey, Integer, String

from app.database.base import Base


class CurrentState(Base):
    __tablename__ = "current_state"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    domain = Column(
        String,
        nullable=False,
    )

    value = Column(
        Float,
        nullable=False,
    )