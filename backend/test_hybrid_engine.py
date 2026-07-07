from app.ai.analysis_result import AnalysisResult
from app.ai.hybrid_impact_engine import HybridImpactEngine

analysis = AnalysisResult(
    sentiment="negative",
    emotion="disappointment",
    confidence=1.0,
    severity="high",
    affected_domains=[
        "Mood",
        "Confidence",
    ],
    reason="Interview failure",
)

engine = HybridImpactEngine()

print(engine.calculate(analysis))