from app.agents.context import AgentContext
from app.agents.twin_agent import TwinAgent
from app.ai.analysis_result import AnalysisResult


class FakeTwinUpdateService:

    def __init__(self):
        self.called_with = None

    def apply_memory(
        self,
        db,
        user_id,
        analysis,
    ):
        self.called_with = {
            "db": db,
            "user_id": user_id,
            "analysis": analysis,
        }

        return {
            "updated": True,
        }


def test_twin_agent_updates_twin():

    service = FakeTwinUpdateService()

    analysis = AnalysisResult(
    emotion="sad",
    sentiment="negative",
    severity="medium",
    confidence=0.9,
    affected_domains=["Sleep"],
)

    context = AgentContext(
        db="fake-db",
        user_id=123,
        memory_analysis=analysis,
    )

    agent = TwinAgent(service=service)

    result = agent.run(context)

    assert result.success is True
    assert result.agent_name == "twin"

    assert result.data == {
        "updated": True,
    }

    assert service.called_with["db"] == "fake-db"
    assert service.called_with["user_id"] == 123
    assert service.called_with["analysis"] == analysis

    assert context.twin_update == {
        "updated": True,
    }


def test_twin_agent_requires_analysis():

    service = FakeTwinUpdateService()

    context = AgentContext(
        db="fake-db",
        user_id=123,
    )

    agent = TwinAgent(service=service)

    result = agent.run(context)

    assert result.success is False
    assert "memory_analysis is required." in result.errors