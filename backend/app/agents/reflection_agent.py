from app.ai.reflection_prompt_builder import ReflectionPromptBuilder
from app.ai.reflection_response_parser import ReflectionResponseParser
from app.llm.ollama_client import OllamaClient

from .base import BaseAgent
from .context import AgentContext
from .result import AgentResult


class ReflectionAgent(BaseAgent):

    name = "reflection"

    def __init__(
        self,
        prompt_builder=None,
        client=None,
        parser=None,
    ):
        self.prompt_builder = (
            prompt_builder
            or ReflectionPromptBuilder()
        )

        self.client = (
            client
            or OllamaClient()
        )

        self.parser = (
            parser
            or ReflectionResponseParser()
        )

    def run(
        self,
        context: AgentContext,
    ) -> AgentResult:

        try:

            # -----------------------------------------
            # Build the context expected by the
            # existing ReflectionPromptBuilder.
            # -----------------------------------------

            reflection_context = {
            "current": context.current_state or [],
            "memories": context.recent_memories or [],
            "snapshots": context.snapshots or [],
            "trend": context.trends or {},
            "decision": context.get_result("decision"),
        }

            # -----------------------------------------
            # Brand-new user
            # -----------------------------------------

            if (
                not reflection_context["current"]
                or (
                    not reflection_context["memories"]
                    and not reflection_context["snapshots"]
                )
            ):

                content = (
                    "Welcome to ECHO! 🌱\n\n"
                    "Your Digital Twin is waiting to learn about you.\n\n"
                    "Start recording memories, setting goals, "
                    "and reflecting on your days. "
                    "As your journey grows, ECHO will begin "
                    "discovering patterns, generating insights, "
                    "and helping you understand yourself better."
                )

                return AgentResult(
                    success=True,
                    agent_name=self.name,
                    data=content,
                    message="Initial reflection generated.",
                )

            # -----------------------------------------
            # Build prompt using existing V1 logic
            # -----------------------------------------

            prompt = self.prompt_builder.build(
                reflection_context,
            )

            raw_response = self.client.generate(
                prompt,
            )

            print(
                "\n========== RAW REFLECTION =========="
            )
            print(raw_response)
            print("===================================\n")

            content = self.parser.parse(
                raw_response,
            )

            return AgentResult(
                success=True,
                agent_name=self.name,
                data=content,
            )

        except Exception as exc:

            return AgentResult(
                success=False,
                agent_name=self.name,
                message="Reflection generation failed.",
                errors=[str(exc)],
            )