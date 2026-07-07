from dataclasses import dataclass
from app.ai.analysis_result import AnalysisResult


@dataclass
class MemoryProcessedEvent:
    db: object
    user_id: int
    memory_id: int
    analysis: AnalysisResult