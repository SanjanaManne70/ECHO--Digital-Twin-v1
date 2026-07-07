from app.agents.insight_agent import InsightAgent
from app.ai.analysis_result import AnalysisResult
from app.database.session import SessionLocal
from app.services.context_service import ContextService


analysis = AnalysisResult(
    sentiment="negative",
    emotion="frustration",
    confidence=0.8,
    severity="high",
    affected_domains=["Learning"],
    reason="Failed coding interview.",
)

db = SessionLocal()

context = ContextService().get_context(
    db,
    user_id=2,
)

agent = InsightAgent()

print("Context built successfully!")

print(context)

print("\nCalling Insight Agent...\n")

response = agent.generate(
    analysis,
    context,
)

print("\nAI RESPONSE:\n")
print(response)