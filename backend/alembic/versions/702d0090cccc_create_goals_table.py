"""create goals table

Revision ID: 702d0090cccc
Revises: b25fe43f77a6
Create Date: 2026-06-28 20:16:40.379636
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "702d0090cccc"
down_revision: Union[str, Sequence[str], None] = "b25fe43f77a6"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "goals",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
        ),

        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id"),
            nullable=False,
        ),

        sa.Column(
            "title",
            sa.String(),
            nullable=False,
        ),

        sa.Column(
            "category",
            sa.String(),
            nullable=False,
        ),

        sa.Column(
            "target_value",
            sa.Float(),
            nullable=False,
        ),

        sa.Column(
            "target_unit",
            sa.String(),
            nullable=False,
        ),

        sa.Column(
            "current_value",
            sa.Float(),
            nullable=False,
            server_default="0",
        ),

        sa.Column(
            "progress",
            sa.Float(),
            nullable=False,
            server_default="0",
        ),

        sa.Column(
            "description",
            sa.Text(),
            nullable=False,
        ),

        sa.Column(
            "ai_reason",
            sa.Text(),
            nullable=True,
        ),

        sa.Column(
            "predicted_completion",
            sa.String(),
            nullable=True,
        ),

        sa.Column(
            "completed",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
        ),
    )


def downgrade() -> None:

    op.drop_table("goals")