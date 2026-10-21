from datetime import date

from app.ai.reflection_context_builder import (
    ReflectionContextBuilder,
)

from app.agents.reflection_agent import (
    ReflectionAgent,
)

from app.models.reflection import Reflection

from app.repositories.reflection_repository import (
    ReflectionRepository,
)
from app.agents.context import AgentContext


class ReflectionService:

    def __init__(self):

        self.context_builder = ReflectionContextBuilder()

        self.agent = ReflectionAgent()

        self.repository = ReflectionRepository()

    # -------------------------------------------------
    # Shared reflection generation logic
    # -------------------------------------------------

    def generate_content(self, context):

        # Brand-new user — don't call the LLM
        if (
            not context["current"]
            or (
                not context["memories"]
                and not context["snapshots"]
            )
        ):
            return (
                "Welcome to ECHO! 🌱\n\n"
                "Your Digital Twin is waiting to learn about you.\n\n"
                "Start recording memories, setting goals, and reflecting on your days. "
                "As your journey grows, ECHO will begin discovering patterns, "
                "generating insights, and helping you understand yourself better."
            )

        agent_context = AgentContext(
            user_id=None,
            current_state=context["current"],
            recent_memories=context["memories"],
            snapshots=context["snapshots"],
            trends=context["trend"],
        )

        result = self.agent.run(agent_context)

        if not result.success:
            error_message = "; ".join(result.errors or [])
            raise RuntimeError(
                error_message or "Reflection generation failed."
            )

        return result.data

    # -------------------------------------------------
    # Dashboard API
    # -------------------------------------------------

    def reflect(
        self,
        db,
        user_id,
    ):

        today = date.today()

        reflection = self.repository.get_by_date(
            db=db,
            user_id=user_id,
            day=today,
        )

        # Cached reflection
        if (
            reflection
            and not reflection.needs_refresh
            and reflection.content
        ):

            return reflection.content

        context = self.context_builder.build(
            db,
            user_id,
        )

        content = self.generate_content(
            context,
        )

        # Update existing reflection
        if reflection:

            reflection.content = content

            reflection.needs_refresh = False

            self.repository.update(
                db,
                reflection,
            )

            return content

        # Create today's reflection
        reflection = Reflection(

            user_id=user_id,

            date=today,

            content=content,

            needs_refresh=False,

        )

        self.repository.create(
            db,
            reflection,
        )

        return content

    # -------------------------------------------------
    # Called after memory is saved
    # -------------------------------------------------

    def refresh_today(
        self,
        db,
        user_id,
    ):

        today = date.today()

        context = self.context_builder.build(
            db,
            user_id,
        )

        content = self.generate_content(
            context,
        )

        reflection = self.repository.get_by_date(
            db=db,
            user_id=user_id,
            day=today,
        )

        if reflection:

            reflection.content = content

            reflection.needs_refresh = False

            return self.repository.update(
                db,
                reflection,
            )

        reflection = Reflection(

            user_id=user_id,

            date=today,

            content=content,

            needs_refresh=False,

        )

        return self.repository.create(
            db,
            reflection,
        )