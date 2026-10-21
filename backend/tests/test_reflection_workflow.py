
from app.agents.context import AgentContext
from app.agents.result import AgentResult
from app.agents.workflows import DEFAULT_MEMORY_WORKFLOW

from app.events.coordinator_handler import CoordinatorHandler
from app.events.events import MemoryProcessedEvent


class FakeDB:
    def __init__(self):
        self.commit_count = 0
        self.rollback_count = 0

    def commit(self):
        self.commit_count += 1

    def rollback(self):
        self.rollback_count += 1


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
        )


class FakeCoordinator:
    def __init__(self):
        self.workflow = None

    def run(self, context, workflow):
        self.workflow = workflow

        return {
            "twin": AgentResult(
                success=True,
                agent_name="twin",
            ),
            "decision": AgentResult(
                success=True,
                agent_name="decision",
                data="decision-result",
            ),
            "reflection": AgentResult(
                success=True,
                agent_name="reflection",
                data="reflection-result",
            ),
        }


class FakeDecisionPersistence:
    def __init__(self):
        self.saved = None

    def save(self, db, user_id, result, commit=True):
        self.saved = result


class FakeGoalPersistence:
    def __init__(self):
        self.saved = None

    def save(self, db, result, user_id=None, commit=True):
        self.saved = (db, result)


class FakeReflectionPersistence:
    def __init__(self):
        self.saved = None

    def save(self, db, user_id, content):
        self.saved = content


def test_reflection_is_part_of_workflow():
    coordinator = FakeCoordinator()

    decision_persistence = FakeDecisionPersistence()
    goal_persistence = FakeGoalPersistence()
    reflection_persistence = FakeReflectionPersistence()

    handler = CoordinatorHandler(
        coordinator=coordinator,
        context_loader=FakeContextLoader(),
        decision_persistence=decision_persistence,
        goal_persistence=goal_persistence,
        reflection_persistence=reflection_persistence,
    )

    # Use a real fake database object, not a string.
    db = FakeDB()

    event = MemoryProcessedEvent(
        db=db,
        user_id=1,
        memory_id=10,
        analysis="fake-analysis",
    )

    results = handler(event)

    # Verify the complete V2 workflow.
    assert coordinator.workflow == DEFAULT_MEMORY_WORKFLOW

    # Verify reflection was executed.
    assert "reflection" in results

    # Verify reflection persistence.
    assert reflection_persistence.saved == "reflection-result"

    # Verify decision persistence.
    assert decision_persistence.saved == "decision-result"

    # Verify goal persistence received the same DB object.
    assert goal_persistence.saved == (
        db,
        "decision-result",
    )
