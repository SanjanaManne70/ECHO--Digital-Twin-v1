
from app.agents.decision_output_router import DecisionOutputRouter


class FakeDB:
    def __init__(self):
        self.commit_count = 0
        self.rollback_count = 0

    def commit(self):
        self.commit_count += 1

    def rollback(self):
        self.rollback_count += 1


class FakeDecisionPersistence:
    def __init__(self):
        self.calls = []

    def save(self, db, user_id, result, commit=True):
        self.calls.append({
            "db": db,
            "user_id": user_id,
            "result": result,
            "commit": commit,
        })


class FakeGoalPersistence:
    def __init__(self):
        self.calls = []

    def save(self, db, result, user_id=None, commit=True):
        self.calls.append({
            "db": db,
            "user_id": user_id,
            "result": result,
            "commit": commit,
        })


def test_router_persists_decision_and_goals():
    decision_persistence = FakeDecisionPersistence()
    goal_persistence = FakeGoalPersistence()
    db = FakeDB()
    result = object()

    router = DecisionOutputRouter(
        decision_persistence=decision_persistence,
        goal_persistence=goal_persistence,
    )

    router.persist(db=db, user_id=1, result=result)

    assert len(decision_persistence.calls) == 1
    assert len(goal_persistence.calls) == 1

    assert decision_persistence.calls[0]["user_id"] == 1
    assert decision_persistence.calls[0]["commit"] is False

    assert goal_persistence.calls[0]["user_id"] == 1
    assert goal_persistence.calls[0]["commit"] is False

    assert db.commit_count == 1
    assert db.rollback_count == 0


def test_router_does_nothing_for_none_result():
    decision_persistence = FakeDecisionPersistence()
    goal_persistence = FakeGoalPersistence()
    db = FakeDB()

    router = DecisionOutputRouter(
        decision_persistence=decision_persistence,
        goal_persistence=goal_persistence,
    )

    router.persist(db=db, user_id=1, result=None)

    assert decision_persistence.calls == []
    assert goal_persistence.calls == []
    assert db.commit_count == 0
    assert db.rollback_count == 0


def test_router_rolls_back_on_persistence_failure():
    class FailingDecisionPersistence:
        def save(self, db, user_id, result, commit=True):
            raise RuntimeError("Persistence failed")

    db = FakeDB()

    router = DecisionOutputRouter(
        decision_persistence=FailingDecisionPersistence(),
        goal_persistence=FakeGoalPersistence(),
    )

    import pytest

    with pytest.raises(RuntimeError, match="Persistence failed"):
        router.persist(db=db, user_id=1, result=object())

    assert db.commit_count == 0
    assert db.rollback_count == 1
