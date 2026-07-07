from dataclasses import dataclass, field


@dataclass
class GoalUpdate:

    goal_id: int

    increment: float

    confidence: float

    reason: str


@dataclass
class GoalMatchResult:

    updates: list[GoalUpdate] = field(default_factory=list)