from app.agents import (
    AgentContext,
    AgentRegistry,
    AgentResult,
    BaseAgent,
)
from types import SimpleNamespace

class TestAgent(BaseAgent):

    name = "test"

    def run(self, context: AgentContext) -> AgentResult:
        return AgentResult(
            success=True,
            agent_name=self.name,
            data={
                "message": "Agent foundation works"
            },
        )


def test_agent_context():
    context = AgentContext()

    assert context.current_state is None
    assert context.recent_memories == []
    assert context.goals == []


def test_agent_result():
    result = AgentResult(
        success=True,
        agent_name="test",
        data={"value": 123},
    )

    assert result.success is True
    assert result.agent_name == "test"
    assert result.data["value"] == 123


def test_agent_registry():

    registry = AgentRegistry()

    agent = TestAgent()

    registry.register(agent)

    assert registry.has("test")

    retrieved = registry.get("test")

    assert retrieved is agent

    assert "test" in registry.list_agents()


def test_agent_execution():

    agent = TestAgent()

    context = AgentContext()

    result = agent.run(context)

    assert result.success is True
    assert result.agent_name == "test"
    assert result.data["message"] == "Agent foundation works"

def test_agent_context_state_lookup():

    context = AgentContext(
        current_state=[
            SimpleNamespace(
                domain="Sleep",
                value=72.5,
            ),
            SimpleNamespace(
                domain="Energy",
                value=61.0,
            ),
        ]
    )

    assert context.get_state("Sleep") == 72.5
    assert context.get_state("sleep") == 72.5
    assert context.get_state("Energy") == 61.0
    assert context.get_state("Mood") is None


def test_agent_context_recent_memory():

    first_memory = SimpleNamespace(
        title="First memory",
    )

    second_memory = SimpleNamespace(
        title="Second memory",
    )

    context = AgentContext(
        recent_memories=[
            first_memory,
            second_memory,
        ]
    )

    assert context.get_recent_memory() is first_memory


def test_agent_context_active_goals():

    active_goal = SimpleNamespace(
        completed=False,
    )

    completed_goal = SimpleNamespace(
        completed=True,
    )

    context = AgentContext(
        goals=[
            completed_goal,
            active_goal,
        ]
    )

    assert context.has_active_goals() is True

    completed_context = AgentContext(
        goals=[
            completed_goal,
        ]
    )

    assert completed_context.has_active_goals() is False