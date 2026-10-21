from app.agents.goal_persistence import GoalPersistence
from app.ai.decision_result import (
    DecisionResult,
    GoalDecision,
)


class FakeGoal:

    def __init__(
        self,
        goal_id,
        target_value,
        current_value,
    ):
        self.id = goal_id
        self.target_value = target_value
        self.current_value = current_value
        self.progress = 0
        self.ai_reason = ""
        self.completed = False


class FakeGoalRepository:

    def __init__(self, goal):
        self.goal = goal

    def get_by_id(self, db, goal_id):
        if goal_id == self.goal.id:
            return self.goal

        return None


class FakeDB:

    def __init__(self):
        self.commit_count = 0

    def commit(self):
        self.commit_count += 1


def test_goal_persistence_updates_goal():

    goal = FakeGoal(
        goal_id=1,
        target_value=100,
        current_value=40,
    )

    repository = FakeGoalRepository(goal)
    persistence = GoalPersistence(
        goal_repo=repository,
    )

    db = FakeDB()

    result = DecisionResult(
        goals=[
            GoalDecision(
                goal_id=1,
                increment=10,
                confidence=0.8,
                reason="Consistent learning activity.",
            )
        ]
    )

    persistence.save(
        db=db,
        result=result,
    )

    assert goal.current_value == 50
    assert goal.progress == 50
    assert goal.ai_reason == "Consistent learning activity."
    assert goal.completed is False
    assert db.commit_count == 1


def test_goal_persistence_ignores_low_confidence_update():

    goal = FakeGoal(
        goal_id=1,
        target_value=100,
        current_value=40,
    )

    repository = FakeGoalRepository(goal)
    persistence = GoalPersistence(
        goal_repo=repository,
    )

    db = FakeDB()

    result = DecisionResult(
        goals=[
            GoalDecision(
                goal_id=1,
                increment=20,
                confidence=0.5,
                reason="Low confidence proposal.",
            )
        ]
    )

    persistence.save(
        db=db,
        result=result,
    )

    assert goal.current_value == 40
    assert goal.progress == 0
    assert db.commit_count == 1


def test_goal_persistence_marks_completed_goal():

    goal = FakeGoal(
        goal_id=1,
        target_value=100,
        current_value=90,
    )

    repository = FakeGoalRepository(goal)
    persistence = GoalPersistence(
        goal_repo=repository,
    )

    db = FakeDB()

    result = DecisionResult(
        goals=[
            GoalDecision(
                goal_id=1,
                increment=10,
                confidence=0.9,
                reason="Goal completed.",
            )
        ]
    )

    persistence.save(
        db=db,
        result=result,
    )

    assert goal.current_value == 100
    assert goal.progress == 100
    assert goal.completed is True