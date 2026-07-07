from app.ai.reflection_context_builder import ReflectionContextBuilder
from app.models.insight import Insight
from app.repositories.insight_repository import InsightRepository
from app.agents.insight_agent import InsightAgent

class InsightService:

    def __init__(self):

        self.agent = InsightAgent()

        self.repository = InsightRepository()

        self.context_builder = ReflectionContextBuilder()

    def generate(
        self,
        db,
        user_id,
        analysis,
    ):

        context = self.context_builder.build(
            db=db,
            user_id=user_id,
        )

        twin = ""

        for state in context["current"]:

            twin += f"{state.domain}: {state.value}\n"

        memories = ""

        for memory in context["memories"]:

            memories += (
                f"- {memory.title}: "
                f"{memory.description}\n"
            )

        text = self.agent.generate(

            analysis=analysis,

            context={
                "twin": twin,
                "memories": memories,
            },
        )

        insight = Insight(

            user_id=user_id,

            title="AI Insight",

            description=text,

            severity=analysis.severity,

        )

        return self.repository.create(
            db,
            insight,
        )