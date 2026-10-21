
from datetime import datetime
from typing import Optional

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class WorkflowRun(Base):
    """Persistent record of one ECHO agent workflow run."""

    __tablename__ = "workflow_runs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Nullable so workflows executed outside a user session can be recorded.
    user_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    workflow_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="custom_workflow",
    )

    status: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="running",
        index=True,
    )

    success: Mapped[Optional[bool]] = mapped_column(
        Boolean,
        nullable=True,
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    finished_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    total_duration_ms: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
    )

    agent_execution_duration_ms: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
    )

    abort_reason: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
