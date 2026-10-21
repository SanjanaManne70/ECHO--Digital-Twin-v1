
from app.agents.context import AgentContext
from app.events.coordinator_handler import CoordinatorHandler
from app.events.events import MemoryProcessedEvent
from app.ai.analysis_result import AnalysisResult


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
        self.saved = None

    def save(self, db, user_id, result, commit=True):
        self.saved = (db, user_id, result)


class FakeGoalPersistence:
    def __init__(self):
        self.saved = None

    def save(self, db, result, user_id=None, commit=True):
        self.saved = (db, result)


class FakeContextLoader:
    def load(
        self,
        db,
        user_id,
        memory_analysis=None,
        memory_id=None,
    ):
        return AgentContext(
            db=db,
            user_id=user_id,
            memory_analysis=memory_analysis,
            metadata={
                "memory_id": memory_id,
            },
        )

    def refresh(self, context):
        return context


class FakeCoordinator:
    def __init__(self):
        self.workflow = None
        self.context = None

    def run(self, context, workflow):
        self.context = context
        self.workflow = workflow

        return {
            "twin": type(
                "FakeResult",
                (),
                {"success": True},
            )(),
            "decision": type(
                "FakeResult",
                (),
                {
                    "success": True,
                    "data": "fake-decision-result",
                },
            )(),
        }


def test_coordinator_handler_builds_context():
    coordinator = FakeCoordinator()

    decision_persistence = FakeDecisionPersistence()
    goal_persistence = FakeGoalPersistence()

    handler = CoordinatorHandler(
        coordinator=coordinator,
        context_loader=FakeContextLoader(),
        decision_persistence=decision_persistence,
        goal_persistence=goal_persistence,
        workflow=["twin", "decision"],
    )

    analysis = AnalysisResult(
        emotion="sad",
        sentiment="negative",
        severity="medium",
        confidence=0.9,
        affected_domains=["Sleep"],
    )

    db = FakeDB()

    event = MemoryProcessedEvent(
        db=db,
        user_id=123,
        memory_id=456,
        analysis=analysis,
    )

    result = handler(event)

    # Workflow was passed correctly
    assert coordinator.workflow == ["twin", "decision"]

    # Shared context was built correctly
    assert coordinator.context.db is db
    assert coordinator.context.user_id == 123
    assert coordinator.context.memory_analysis == analysis
    assert coordinator.context.metadata["memory_id"] == 456

    # Both agents completed successfully
    assert result["twin"].success is True
    assert result["decision"].success is True

    # Decision persistence received the result
    assert decision_persistence.saved == (
        db,
        123,
        "fake-decision-result",
    )

    # Goal persistence received the decision result
    assert goal_persistence.saved == (
        db,
        "fake-decision-result",
    )
