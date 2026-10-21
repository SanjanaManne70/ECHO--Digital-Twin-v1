from app.ai.trend_analyzer import TrendAnalyzer

from .base import BaseAgent
from .context import AgentContext
from .result import AgentResult


class TrendAgent(BaseAgent):

    name = "trend"

    def __init__(self, analyzer=None):
        self.analyzer = analyzer or TrendAnalyzer()

    def run(self, context: AgentContext) -> AgentResult:

        try:
            trends = self.analyzer.analyze(
                snapshots=context.snapshots
            )

            context.trends = trends

            return AgentResult(
                success=True,
                agent_name=self.name,
                data=trends,
            )

        except Exception as exc:
            return AgentResult(
                success=False,
                agent_name=self.name,
                message="Trend analysis failed.",
                errors=[str(exc)],
            )