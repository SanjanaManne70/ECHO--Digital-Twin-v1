from app.agents.coordinator import Coordinator
from app.agents.registry import AgentRegistry
from app.agents.twin_agent import TwinAgent
from app.agents.decision_agent import DecisionAgent
from app.events.coordinator_handler import CoordinatorHandler
from app.events.events import MemoryProcessedEvent
from app.ai.analysis_result import AnalysisResult
from app.ai.decision_result import (
    DecisionResult,
    InsightDecision,
    PlannerDecision,
)
from app.agents.context import AgentContext


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
            metadata={"memory_id": memory_id},
        )

    def refresh(self, context):
        return context


class FakeTwinUpdateService:
    def __init__(self):
        self.call_count = 0

    def apply_memory(self, db, user_id, analysis):
        self.call_count += 1

        return {
            "updated": True,
        }


class FakeDecisionEngine:
    def __init__(self):
        self.call_count = 0
        self.last_call = None

    def decide(
        self,
        analysis,
        goals,
        trend,
        memories,
        state,
    ):
        self.call_count += 1

        self.last_call = {
            "analysis": analysis,
            "goals": goals,
            "trend": trend,
            "memories": memories,
            "state": state,
        }

        return DecisionResult(
            insight=InsightDecision(
                title="Sleep Insight",
                description="Sleep may be affecting energy.",
                severity="medium",
            ),
            planner=PlannerDecision(
                title="Improve Sleep",
                description="Maintain a consistent sleep schedule.",
                priority="high",
            ),
        )


class FakeDecisionPersistence:
    def __init__(self):
        self.call_count = 0
        self.last_call = None

    def save(self, db, user_id, result, commit=True):
        self.call_count += 1

        self.last_call = {
            "db": db,
            "user_id": user_id,
            "result": result,
        }


class FakeGoalPersistence:
    def __init__(self):
        self.call_count = 0
        self.last_call = None

    def save(self, db, result, user_id=None, commit=True):
        self.call_count += 1

        self.last_call = {
            "db": db,
            "result": result,
        }


def test_twin_and_decision_agents_run_in_one_workflow():
    # Arrange
    twin_service = FakeTwinUpdateService()
    decision_engine = FakeDecisionEngine()

    persistence = FakeDecisionPersistence()
    goal_persistence = FakeGoalPersistence()

    twin_agent = TwinAgent(
        service=twin_service,
    )

    decision_agent = DecisionAgent(
        engine=decision_engine,
    )

    registry = AgentRegistry()
    registry.register(twin_agent)
    registry.register(decision_agent)

    # Share the context loader between the coordinator
    # and the event handler.
    context_loader = FakeContextLoader()

    coordinator = Coordinator(
        registry=registry,
        context_loader=context_loader,
    )

    handler = CoordinatorHandler(
        coordinator=coordinator,
        context_loader=context_loader,
        decision_persistence=persistence,
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

    # Act
    results = handler(event)

    # Assert: TwinAgent ran exactly once
    assert twin_service.call_count == 1

    # Assert: DecisionAgent ran exactly once
    assert decision_engine.call_count == 1

    # DecisionAgent received the shared memory analysis
    assert decision_engine.last_call["analysis"] == analysis

    # Both agents completed successfully
    assert results["twin"].success is True
    assert results["decision"].success is True

    # Decision result was persisted exactly once
    assert persistence.call_count == 1
    assert persistence.last_call["db"] is db
    assert persistence.last_call["user_id"] == 123
    assert persistence.last_call["result"] == results["decision"].data

    # Goal persistence was called exactly once
    assert goal_persistence.call_count == 1
    assert goal_persistence.last_call["db"] is db
    assert goal_persistence.last_call["result"] == results["decision"].data
