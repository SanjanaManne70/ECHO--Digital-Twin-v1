from app.agents import AgentContext, MemoryAgent
from app.ai.analysis_result import AnalysisResult


class FakeMemoryAnalyzer:

    def analyze(self, title, description):

        return AnalysisResult(
            sentiment="positive",
            emotion="motivated",
            confidence=0.95,
            severity="low",
            affected_domains=["Learning"],
            reason="The memory describes productive learning.",
        )


def test_memory_agent_analyzes_memory():

    analyzer = FakeMemoryAnalyzer()

    agent = MemoryAgent(
        analyzer=analyzer,
    )

    context = AgentContext(
        current_memory={
            "title": "DSA Practice",
            "description": "I solved three dynamic programming problems.",
        }
    )

    result = agent.run(context)

    assert result.success is True

    assert result.agent_name == "memory"

    assert result.data.sentiment == "positive"

    assert result.data.emotion == "motivated"

    assert result.data.affected_domains == ["Learning"]


def test_memory_agent_updates_context():

    analyzer = FakeMemoryAnalyzer()

    agent = MemoryAgent(
        analyzer=analyzer,
    )

    context = AgentContext(
        current_memory={
            "title": "Study",
            "description": "Studied algorithms.",
        }
    )

    result = agent.run(context)

    assert result.success is True

    assert context.memory_analysis is result.data


def test_memory_agent_requires_memory():

    analyzer = FakeMemoryAnalyzer()

    agent = MemoryAgent(
        analyzer=analyzer,
    )

    context = AgentContext()

    result = agent.run(context)

    assert result.success is False

    assert result.agent_name == "memory"

    assert "current_memory is required." in result.errors