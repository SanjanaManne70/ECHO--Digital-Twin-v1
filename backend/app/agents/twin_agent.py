from app.services.twin_update_service import TwinUpdateService

from .base import BaseAgent
from .context import AgentContext
from .result import AgentResult


class TwinAgent(BaseAgent):

    name = "twin"

    def __init__(
        self,
        service: TwinUpdateService | None = None,
    ):
        self.service = service or TwinUpdateService()

    def run(
        self,
        context: AgentContext,
    ) -> AgentResult:

        if context.db is None:
            return AgentResult(
                success=False,
                agent_name=self.name,
                message="Database session is required.",
                errors=["db is required."],
            )

        if context.user_id is None:
            return AgentResult(
                success=False,
                agent_name=self.name,
                message="User ID is required.",
                errors=["user_id is required."],
            )

        if context.memory_analysis is None:
            return AgentResult(
                success=False,
                agent_name=self.name,
                message="Memory analysis is required.",
                errors=["memory_analysis is required."],
            )

        try:

            result = self.service.apply_memory(
                db=context.db,
                user_id=context.user_id,
                analysis=context.memory_analysis,
            )

            context.twin_update = result

            return AgentResult(
                success=True,
                agent_name=self.name,
                data=result,
            )

        except Exception as exc:

            return AgentResult(
                success=False,
                agent_name=self.name,
                message="Twin update failed.",
                errors=[str(exc)],
            )