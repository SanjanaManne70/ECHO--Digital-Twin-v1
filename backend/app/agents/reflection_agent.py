from app.ai.reflection_prompt_builder import (
    ReflectionPromptBuilder,
)

from app.ai.reflection_response_parser import (
    ReflectionResponseParser,
)

from app.llm.ollama_client import OllamaClient


class ReflectionAgent:

    def __init__(self):

        self.prompt_builder = ReflectionPromptBuilder()

        self.client = OllamaClient()

        self.parser = ReflectionResponseParser()

    def reflect(
        self,
        context,
    ):

        prompt = self.prompt_builder.build(
            context,
        )

        raw_response = self.client.generate(
            prompt,
        )

        print("\n========== RAW REFLECTION ==========")
        print(raw_response)
        print("===================================\n")

        return self.parser.parse(
            raw_response,
        )