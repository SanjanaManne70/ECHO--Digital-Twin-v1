from app.ai.decision_engine import DecisionEngine

from .base import BaseAgent
from .context import AgentContext
from .result import AgentResult


class DecisionAgent(BaseAgent):

    name = "decision"

    def __init__(
        self,
        engine: DecisionEngine | None = None,
    ):
        self.engine = engine or DecisionEngine()

    def run(
        self,
        context: AgentContext,
    ) -> AgentResult:

        if context.memory_analysis is None:
            return AgentResult(
                success=False,
                agent_name=self.name,
                message="Memory analysis is required.",
                errors=["memory_analysis is required."],
            )

        try:

            result = self.engine.decide(
                analysis=context.memory_analysis,
                goals=context.goals,
                trend=context.trends,
                memories=context.recent_memories,
                state=context.current_state,
            )

            return AgentResult(
                success=True,
                agent_name=self.name,
                data=result,
            )

        except Exception as exc:

            return AgentResult(
                success=False,
                agent_name=self.name,
                message="Decision generation failed.",
                errors=[str(exc)],
            )