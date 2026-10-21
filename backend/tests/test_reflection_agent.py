from app.agents.context import AgentContext
from app.agents.reflection_agent import ReflectionAgent


class FakePromptBuilder:

    def build(self, context):
        return "fake reflection prompt"


class FakeClient:

    def generate(self, prompt):
        assert prompt == "fake reflection prompt"
        return "RAW REFLECTION"


class FakeParser:

    def parse(self, response):
        assert response == "RAW REFLECTION"
        return "Final reflection"


def test_reflection_agent():

    agent = ReflectionAgent(
        prompt_builder=FakePromptBuilder(),
        client=FakeClient(),
        parser=FakeParser(),
    )

    context = AgentContext(
        current_state=[
            type(
                "State",
                (),
                {
                    "domain": "Learning",
                    "value": 80,
                },
            )()
        ],
        recent_memories=[
            type(
                "Memory",
                (),
                {
                    "title": "Completed ECHO V2",
                    "description": "Finished multi-agent architecture.",
                },
            )()
        ],
        snapshots=[],
        trends={
            "learning_change": 10,
        },
    )

    result = agent.run(context)

    assert result.success is True
    assert result.agent_name == "reflection"
    assert result.data == "Final reflection"

def test_reflection_agent_receives_decision_result():

    captured_context = {}

    class DecisionAwarePromptBuilder:

        def build(self, context):
            captured_context.update(context)
            return "decision-aware prompt"

    class FakeClient:

        def generate(self, prompt):
            assert prompt == "decision-aware prompt"
            return "RAW REFLECTION"

    class FakeParser:

        def parse(self, response):
            return "Reflection with decision"

    agent = ReflectionAgent(
        prompt_builder=DecisionAwarePromptBuilder(),
        client=FakeClient(),
        parser=FakeParser(),
    )

    decision_result = type(
        "DecisionResult",
        (),
        {
            "success": True,
            "data": "decision-output",
        },
    )()

    context = AgentContext(
        current_state=[
            type(
                "State",
                (),
                {
                    "domain": "Learning",
                    "value": 80,
                },
            )()
        ],
        recent_memories=[
            type(
                "Memory",
                (),
                {
                    "title": "Completed ECHO V2",
                    "description": "Finished multi-agent architecture.",
                },
            )()
        ],
        snapshots=[],
        trends={},
    )

    context.store_result(
        "decision",
        decision_result,
    )

    result = agent.run(context)

    assert result.success is True
    assert result.data == "Reflection with decision"

    assert captured_context["decision"] is decision_result