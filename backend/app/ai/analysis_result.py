from dataclasses import dataclass, field


@dataclass
class AnalysisResult:
    sentiment: str
    emotion: str
    confidence: float
    severity: str
    affected_domains: list[str] = field(default_factory=list)
    reason: str = ""