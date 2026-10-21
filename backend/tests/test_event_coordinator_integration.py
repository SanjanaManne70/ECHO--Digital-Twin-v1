from app.agents.coordinator import Coordinator
from app.agents.registry import AgentRegistry
from app.agents.twin_agent import TwinAgent
from app.events.coordinator_handler import CoordinatorHandler
from app.events.events import MemoryProcessedEvent
from app.ai.analysis_result import AnalysisResult
from app.agents.context import AgentContext

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
    
class FakeTwinUpdateService:

    def __init__(self):
        self.call_count = 0
        self.last_call = None

    def apply_memory(
        self,
        db,
        user_id,
        analysis,
    ):
        self.call_count += 1

        self.last_call = {
            "db": db,
            "user_id": user_id,
            "analysis": analysis,
        }

        return {
            "updated": True,
        }


def test_event_flows_through_coordinator_to_twin():

    service = FakeTwinUpdateService()

    twin_agent = TwinAgent(
        service=service,
    )

    registry = AgentRegistry()

    registry.register(
        twin_agent,
    )

    coordinator = Coordinator(
        registry=registry,
    )

    handler = CoordinatorHandler(
    coordinator=coordinator,
    context_loader=FakeContextLoader(),
    workflow=["twin"],
)

    analysis = AnalysisResult(
        emotion="sad",
        sentiment="negative",
        severity="medium",
        confidence=0.9,
        affected_domains=["Sleep"],
    )

    event = MemoryProcessedEvent(
        db="fake-db",
        user_id=123,
        memory_id=456,
        analysis=analysis,
    )

    results = handler(event)

    assert service.call_count == 1

    assert service.last_call["db"] == "fake-db"
    assert service.last_call["user_id"] == 123
    assert service.last_call["analysis"] == analysis

    assert results["twin"].success is True

    assert results["twin"].data == {
        "updated": True,
    }