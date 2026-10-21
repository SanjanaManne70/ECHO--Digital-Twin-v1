
from app.agents.decision_persistence import DecisionPersistence
from app.ai.decision_result import (
    DecisionResult,
    InsightDecision,
    PlannerDecision,
)


class FakeInsightRepository:
    def __init__(self):
        self.created = []

    def create(self, db, insight, commit=True):
        self.created.append(insight)

        if commit:
            db.commit()

        return insight


class FakePlannerRepository:
    def __init__(self):
        self.created = []

    def create(self, db, planner, commit=True):
        self.created.append(planner)

        if commit:
            db.commit()

        return planner


class FakeDB:
    def __init__(self):
        self.commit_called = False
        self.commit_count = 0

    def commit(self):
        self.commit_called = True
        self.commit_count += 1


def test_decision_persistence_saves_insight_and_planner():
    insight_repo = FakeInsightRepository()
    planner_repo = FakePlannerRepository()

    persistence = DecisionPersistence(
        insight_repo=insight_repo,
        planner_repo=planner_repo,
    )

    db = FakeDB()

    result = DecisionResult(
        insight=InsightDecision(
            title="Sleep Insight",
            description="Your recent sleep pattern may affect energy.",
            severity="medium",
        ),
        planner=PlannerDecision(
            title="Improve Sleep",
            description="Maintain a consistent sleep schedule.",
            priority="high",
        ),
    )

    persistence.save(
        db=db,
        user_id=123,
        result=result,
    )

    assert len(insight_repo.created) == 1
    assert len(planner_repo.created) == 1

    assert insight_repo.created[0].user_id == 123
    assert insight_repo.created[0].title == "Sleep Insight"

    assert planner_repo.created[0].user_id == 123
    assert planner_repo.created[0].title == "Improve Sleep"

    # DecisionPersistence performs one final commit.
    assert db.commit_called is True
    assert db.commit_count == 1


def test_decision_persistence_defers_commit_when_requested():
    insight_repo = FakeInsightRepository()
    planner_repo = FakePlannerRepository()

    persistence = DecisionPersistence(
        insight_repo=insight_repo,
        planner_repo=planner_repo,
    )

    db = FakeDB()

    result = DecisionResult(
        insight=InsightDecision(
            title="Sleep Insight",
            description="Your recent sleep pattern may affect energy.",
            severity="medium",
        ),
        planner=PlannerDecision(
            title="Improve Sleep",
            description="Maintain a consistent sleep schedule.",
            priority="high",
        ),
    )

    persistence.save(
        db=db,
        user_id=123,
        result=result,
        commit=False,
    )

    assert len(insight_repo.created) == 1
    assert len(planner_repo.created) == 1

    # The router will commit after all persistence operations succeed.
    assert db.commit_called is False
    assert db.commit_count == 0
