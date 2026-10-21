from app.agents import (
    AgentContext,
    AgentRegistry,
    AgentResult,
    BaseAgent,
    Coordinator,
    AgentStep,
)


# =========================================================
# TEST AGENTS
# =========================================================

class FailingAgent(BaseAgent):

    name = "failing_agent"

    def run(self, context: AgentContext) -> AgentResult:
        return AgentResult(
            success=False,
            agent_name=self.name,
            message="Intentional failure.",
            errors=["Test failure"],
        )


class ExceptionAgent(BaseAgent):

    name = "exception_agent"

    def run(self, context: AgentContext) -> AgentResult:
        raise RuntimeError("Unexpected agent exception")


class DependentAgent(BaseAgent):

    name = "dependent_agent"

    def run(self, context: AgentContext) -> AgentResult:
        return AgentResult(
            success=True,
            agent_name=self.name,
            data={
                "executed": True
            },
        )


class TestAgentA(BaseAgent):

    name = "agent_a"

    def run(self, context: AgentContext) -> AgentResult:
        return AgentResult(
            success=True,
            agent_name=self.name,
            data={
                "value": 100
            },
        )


class TestAgentB(BaseAgent):

    name = "agent_b"

    def run(self, context: AgentContext) -> AgentResult:

        previous_result = context.get_result("agent_a")

        previous_value = previous_result.data["value"]

        return AgentResult(
            success=True,
            agent_name=self.name,
            data={
                "received_value": previous_value,
                "value": previous_value + 50,
            },
        )


# =========================================================
# DEPENDENCY TESTS
# =========================================================

def test_agent_dependency_allows_execution_when_dependency_succeeds():

    registry = AgentRegistry()

    registry.register(TestAgentA())
    registry.register(DependentAgent())

    coordinator = Coordinator(registry)

    context = AgentContext()

    results = coordinator.run(
        context=context,
        workflow=[
            AgentStep("agent_a"),
            AgentStep(
                "dependent_agent",
                depends_on=["agent_a"],
            ),
        ],
    )

    assert results["agent_a"].success is True
    assert results["dependent_agent"].success is True

    assert results["dependent_agent"].data["executed"] is True


def test_agent_dependency_skips_when_dependency_fails():

    registry = AgentRegistry()

    registry.register(FailingAgent())
    registry.register(DependentAgent())

    coordinator = Coordinator(registry)

    context = AgentContext()

    results = coordinator.run(
        context=context,
        workflow=[
            AgentStep("failing_agent"),
            AgentStep(
                "dependent_agent",
                depends_on=["failing_agent"],
            ),
        ],
    )

    assert results["failing_agent"].success is False

    dependent_result = results["dependent_agent"]

    assert dependent_result.success is False
    assert dependent_result.metadata["skipped"] is True

    assert dependent_result.message == (
        "Agent skipped because a dependency failed."
    )


def test_agent_can_run_when_dependency_failed_if_configured():

    registry = AgentRegistry()

    registry.register(FailingAgent())
    registry.register(DependentAgent())

    coordinator = Coordinator(registry)

    context = AgentContext()

    results = coordinator.run(
        context=context,
        workflow=[
            AgentStep("failing_agent"),
            AgentStep(
                "dependent_agent",
                depends_on=["failing_agent"],
                run_if_dependencies_failed=True,
            ),
        ],
    )

    assert results["failing_agent"].success is False
    assert results["dependent_agent"].success is True

    assert results["dependent_agent"].data["executed"] is True


# =========================================================
# WORKFLOW EXECUTION TESTS
# =========================================================

def test_coordinator_executes_workflow():

    registry = AgentRegistry()

    registry.register(TestAgentA())
    registry.register(TestAgentB())

    coordinator = Coordinator(registry)

    context = AgentContext()

    results = coordinator.run(
        context=context,
        workflow=[
            "agent_a",
            "agent_b",
        ],
    )

    assert "agent_a" in results
    assert "agent_b" in results

    assert results["agent_a"].success is True
    assert results["agent_b"].success is True


def test_agent_results_are_propagated():

    registry = AgentRegistry()

    registry.register(TestAgentA())
    registry.register(TestAgentB())

    coordinator = Coordinator(registry)

    context = AgentContext()

    coordinator.run(
        context=context,
        workflow=[
            "agent_a",
            "agent_b",
        ],
    )

    # Agent A's result should be stored.
    assert context.get_result("agent_a") is not None

    # Agent B should have received Agent A's result.
    agent_b_result = context.get_result("agent_b")

    assert agent_b_result is not None

    assert agent_b_result.data["received_value"] == 100
    assert agent_b_result.data["value"] == 150


# =========================================================
# CONTEXT REFRESH TEST
# =========================================================

class FakeRefreshLoader:

    def __init__(self):
        self.refresh_count = 0

    def refresh(self, context):
        self.refresh_count += 1

        context.current_state = {
            "Learning": 97
        }

        return context


def test_coordinator_refreshes_context_between_agents():

    registry = AgentRegistry()

    registry.register(TestAgentA())
    registry.register(TestAgentB())

    context_loader = FakeRefreshLoader()

    coordinator = Coordinator(
        registry=registry,
        context_loader=context_loader,
    )

    context = AgentContext()

    coordinator.run(
        context=context,
        workflow=[
            "agent_a",
            "agent_b",
        ],
    )

    assert context_loader.refresh_count == 1

    assert context.current_state == {
        "Learning": 97
    }


# =========================================================
# WORKFLOW VALIDATION TESTS
# =========================================================

def test_coordinator_rejects_unregistered_agent():

    registry = AgentRegistry()

    registry.register(TestAgentA())

    coordinator = Coordinator(registry)

    context = AgentContext()

    try:

        coordinator.run(
            context=context,
            workflow=[
                AgentStep("unknown_agent"),
            ],
        )

        assert False, "Expected KeyError"

    except KeyError as exc:

        assert "unknown_agent" in str(exc)


def test_coordinator_rejects_missing_dependency():

    registry = AgentRegistry()

    registry.register(TestAgentA())
    registry.register(TestAgentB())

    coordinator = Coordinator(registry)

    context = AgentContext()

    try:

        coordinator.run(
            context=context,
            workflow=[
                AgentStep(
                    "agent_b",
                    depends_on=["missing_agent"],
                ),
            ],
        )

        assert False, "Expected ValueError"

    except ValueError as exc:

        assert "missing_agent" in str(exc)


def test_coordinator_rejects_duplicate_agents():

    registry = AgentRegistry()

    registry.register(TestAgentA())
    registry.register(TestAgentB())

    coordinator = Coordinator(registry)

    context = AgentContext()

    try:

        coordinator.run(
            context=context,
            workflow=[
                AgentStep("agent_a"),
                AgentStep("agent_a"),
            ],
        )

        assert False, "Expected ValueError"

    except ValueError as exc:

        assert "agent_a" in str(exc)


def test_coordinator_rejects_dependency_defined_after_agent():

    registry = AgentRegistry()

    registry.register(TestAgentA())
    registry.register(TestAgentB())

    coordinator = Coordinator(registry)

    context = AgentContext()

    try:

        coordinator.run(
            context=context,
            workflow=[
                AgentStep(
                    "agent_b",
                    depends_on=["agent_a"],
                ),
                AgentStep("agent_a"),
            ],
        )

        assert False, "Expected ValueError"

    except ValueError as exc:

        assert "agent_a" in str(exc)


# =========================================================
# AGENT FAILURE ISOLATION TEST
# =========================================================

def test_coordinator_catches_agent_exception():

    registry = AgentRegistry()

    exception_agent = ExceptionAgent()

    registry.register(
        exception_agent
    )

    coordinator = Coordinator(
        registry=registry
    )

    context = AgentContext()

    results = coordinator.run(
        context=context,
        workflow=[
            exception_agent.name
        ]
    )

    result = results[
        exception_agent.name
    ]

    assert result.success is False

    assert result.agent_name == (
        exception_agent.name
    )

    assert result.message == (
        f"Agent '{exception_agent.name}' "
        "failed during execution."
    )

    assert len(result.errors) == 1

    assert result.errors[0] == (
        "Unexpected agent exception"
    )

    assert result.metadata[
        "exception_type"
    ] == "RuntimeError"

def test_coordinator_records_execution_trace():

    registry = AgentRegistry()

    registry.register(TestAgentA())
    registry.register(TestAgentB())

    coordinator = Coordinator(
        registry=registry
    )

    context = AgentContext()

    coordinator.run(
        context=context,
        workflow=[
            "agent_a",
            "agent_b",
        ],
    )

    trace = context.metadata[
        "execution_trace"
    ]

    assert trace is not None

    assert len(
        trace.executions
    ) == 2

    agent_a_execution = trace.get(
        "agent_a"
    )

    agent_b_execution = trace.get(
        "agent_b"
    )

    assert agent_a_execution is not None
    assert agent_b_execution is not None

    assert agent_a_execution.success is True
    assert agent_b_execution.success is True

    assert agent_a_execution.duration_ms >= 0
    assert agent_b_execution.duration_ms >= 0

    assert trace.total_duration_ms >= 0

    assert trace.success is True

def test_coordinator_records_skipped_execution():

    registry = AgentRegistry()

    registry.register(FailingAgent())
    registry.register(DependentAgent())

    coordinator = Coordinator(
        registry=registry
    )

    context = AgentContext()

    coordinator.run(
        context=context,
        workflow=[
            AgentStep(
                "failing_agent"
            ),
            AgentStep(
                "dependent_agent",
                depends_on=[
                    "failing_agent"
                ],
            ),
        ],
    )

    trace = context.metadata[
        "execution_trace"
    ]

    execution = trace.get(
        "dependent_agent"
    )

    assert execution is not None

    assert execution.success is False

    assert execution.skipped is True

    assert execution.duration_ms == 0.0

    assert trace.success is False


def test_coordinator_handles_invalid_agent_result():
    class InvalidAgent(BaseAgent):
        name = "invalid_agent"

        def run(self, context):
            return None

    registry = AgentRegistry()
    registry.register(InvalidAgent())

    context = AgentContext()
    coordinator = Coordinator(registry)

    results = coordinator.run(context, ["invalid_agent"])

    assert results["invalid_agent"].success is False
    assert results["invalid_agent"].metadata["exception_type"] == "TypeError"

    trace = context.metadata["execution_trace"]
    assert trace.get("invalid_agent").status == "failed"


def test_context_refresh_failure_records_remaining_agents():
    class BrokenRefreshLoader:
        def refresh(self, context):
            raise RuntimeError("Refresh unavailable")

    registry = AgentRegistry()
    registry.register(TestAgentA())
    registry.register(TestAgentB())

    context = AgentContext()
    coordinator = Coordinator(
        registry=registry,
        context_loader=BrokenRefreshLoader(),
    )

    results = coordinator.run(context, ["agent_a", "agent_b"])

    assert results["agent_a"].success is True
    assert results["agent_b"].success is False
    assert results["agent_b"].metadata["not_run"] is True

    trace = context.metadata["execution_trace"]
    assert trace.workflow_status == "aborted"
    assert trace.success is False
    assert trace.get("agent_b").status == "not_run"
    assert trace.abort_reason is not None


def test_trace_separates_agent_and_workflow_durations():
    registry = AgentRegistry()
    registry.register(TestAgentA())

    context = AgentContext()
    coordinator = Coordinator(registry)

    coordinator.run(context, ["agent_a"])

    trace = context.metadata["execution_trace"]
    data = trace.to_dict()

    assert data["total_duration_ms"] >= 0
    assert data["agent_execution_duration_ms"] >= 0
    assert data["workflow_status"] == "completed"
    assert data["agent_count"] == 1
    assert data["executions"][0]["status"] == "succeeded"
