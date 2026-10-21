
from app.agents.execution import AgentExecution, ExecutionTrace


def test_successful_execution_trace():
    trace = ExecutionTrace()
    trace.add(
        AgentExecution(
            agent_name="twin_agent",
            success=True,
            duration_ms=12.5,
        )
    )

    assert trace.success is True
    assert trace.get("twin_agent").status == "succeeded"


def test_failed_execution_makes_trace_unsuccessful():
    trace = ExecutionTrace()
    trace.add(
        AgentExecution("twin_agent", True, 12.5)
    )
    trace.add(
        AgentExecution(
            "decision_agent",
            False,
            5.0,
            error="Decision failed",
        )
    )

    assert trace.success is False
    assert trace.get("decision_agent").status == "failed"


def test_all_skipped_trace_is_unsuccessful():
    trace = ExecutionTrace()
    trace.add(
        AgentExecution(
            agent_name="reflection_agent",
            success=False,
            duration_ms=0.0,
            skipped=True,
        )
    )

    assert trace.success is False
    assert trace.get("reflection_agent").status == "skipped"


def test_trace_serialization():
    trace = ExecutionTrace()
    trace.add(
        AgentExecution(
            agent_name="twin_agent",
            success=True,
            duration_ms=12.5678,
        )
    )

    data = trace.to_dict()

    assert data["success"] is True
    assert data["agent_count"] == 1
    assert data["executions"][0]["agent_name"] == "twin_agent"
    assert data["executions"][0]["status"] == "succeeded"
    assert data["executions"][0]["duration_ms"] == 12.5678
