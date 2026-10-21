from app.agents.workflow import AgentStep
from app.agents.workflows import DEFAULT_MEMORY_WORKFLOW


def test_default_memory_workflow_structure():

    assert len(DEFAULT_MEMORY_WORKFLOW) == 4

    assert DEFAULT_MEMORY_WORKFLOW[0] == AgentStep(
        agent_name="twin"
    )

    assert DEFAULT_MEMORY_WORKFLOW[1] == AgentStep(
        agent_name="trend",
        depends_on=["twin"],
    )

    assert DEFAULT_MEMORY_WORKFLOW[2] == AgentStep(
        agent_name="decision",
        depends_on=["trend"],
    )

    assert DEFAULT_MEMORY_WORKFLOW[3] == AgentStep(
        agent_name="reflection",
        depends_on=["decision"],
    )