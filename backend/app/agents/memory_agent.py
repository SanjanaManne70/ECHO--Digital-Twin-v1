from app.ai.memory_analyzer import MemoryAnalyzer

from .base import BaseAgent
from .context import AgentContext
from .result import AgentResult


class MemoryAgent(BaseAgent):
    """
    ECHO V2 Memory Agent.

    This agent adapts the existing V1 MemoryAnalyzer to the
    common V2 agent interface.

    It does not directly handle database persistence or events.
    """

    name = "memory"

    def __init__(self, analyzer: MemoryAnalyzer | None = None):
        self.analyzer = analyzer or MemoryAnalyzer()

    def run(self, context: AgentContext) -> AgentResult:
        """
        Analyze the current memory stored in AgentContext.
        """

        memory = context.current_memory

        if memory is None:
            return AgentResult(
                success=False,
                agent_name=self.name,
                message="No current memory provided.",
                errors=["current_memory is required."],
            )

        try:
            analysis = self.analyzer.analyze(
                title=memory["title"],
                description=memory["description"],
            )

            context.memory_analysis = analysis

            return AgentResult(
                success=True,
                agent_name=self.name,
                data=analysis,
            )

        except Exception as exc:
            return AgentResult(
                success=False,
                agent_name=self.name,
                message="Memory analysis failed.",
                errors=[str(exc)],
            )