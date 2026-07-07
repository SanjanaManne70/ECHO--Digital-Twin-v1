from dataclasses import dataclass, field


@dataclass
class OverallPrediction:

    status: str

    confidence: float

    summary: str


@dataclass
class DomainPrediction:

    name: str

    current: str

    future: str

    trend: str


@dataclass
class GoalPrediction:

    title: str

    current_progress: float

    future_progress: float

    completion: str


@dataclass
class SimulationResult:

    overall: OverallPrediction | None = None

    domains: list[DomainPrediction] = field(default_factory=list)

    goals: list[GoalPrediction] = field(default_factory=list)

    benefits: list[str] = field(default_factory=list)

    risks: list[str] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)