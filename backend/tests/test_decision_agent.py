from app.agents.context import AgentContext
from app.agents.decision_agent import DecisionAgent
from app.ai.analysis_result import AnalysisResult


class FakeDecisionEngine:

    def __init__(self):
        self.called_with = None

    def decide(
        self,
        analysis,
        goals,
        trend,
        memories,
        state,
    ):

        self.called_with = {
            "analysis": analysis,
            "goals": goals,
            "trend": trend,
            "memories": memories,
            "state": state,
        }

        return {
            "decision": "test-result",
        }


def test_decision_agent_uses_shared_context():

    engine = FakeDecisionEngine()

    analysis = AnalysisResult(
        emotion="sad",
        sentiment="negative",
        severity="medium",
        confidence=0.9,
        affected_domains=["Sleep"],
    )

    context = AgentContext(
        memory_analysis=analysis,
        goals=["goal-1"],
        trends={"sleep_change": -2},
        recent_memories=["memory-1"],
        current_state={
            "Sleep": 40,
            "Energy": 45,
        },
    )

    agent = DecisionAgent(
        engine=engine,
    )

    result = agent.run(context)

    assert result.success is True

    assert result.agent_name == "decision"

    assert result.data == {
        "decision": "test-result",
    }

    assert engine.called_with["analysis"] == analysis
    assert engine.called_with["goals"] == ["goal-1"]
    assert engine.called_with["trend"] == {
        "sleep_change": -2,
    }
    assert engine.called_with["memories"] == ["memory-1"]

    assert engine.called_with["state"] == {
        "Sleep": 40,
        "Energy": 45,
    }


def test_decision_agent_requires_analysis():

    engine = FakeDecisionEngine()

    context = AgentContext()

    agent = DecisionAgent(
        engine=engine,
    )

    result = agent.run(context)

    assert result.success is False

    assert "memory_analysis is required." in result.errors