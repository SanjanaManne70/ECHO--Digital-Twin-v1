from dataclasses import dataclass, field


@dataclass
class PlannerDecision:

    title: str

    description: str

    priority: str


@dataclass
class InsightDecision:

    title: str

    description: str

    severity: str


@dataclass
class GoalDecision:

    goal_id: int

    increment: float

    confidence: float

    reason: str


@dataclass
class DecisionResult:

    planner: PlannerDecision | None = None

    insight: InsightDecision | None = None

    goals: list[GoalDecision] = field(default_factory=list)