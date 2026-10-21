from .workflow import AgentStep


DEFAULT_MEMORY_WORKFLOW = [
    AgentStep("twin"),
    AgentStep("trend", depends_on=["twin"]),
    AgentStep("decision", depends_on=["trend"]),
    AgentStep("reflection", depends_on=["decision"]),
]