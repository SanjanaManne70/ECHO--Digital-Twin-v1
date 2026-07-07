from app.ai.prompt_builder import PromptBuilder
from app.ai.response_parser import ResponseParser
from app.ai.analysis_result import AnalysisResult
from app.llm.ollama_client import OllamaClient


class MemoryAnalyzer:

    def __init__(self):

        self.prompt_builder = PromptBuilder()
        self.client = OllamaClient()
        self.parser = ResponseParser()

    def analyze(
        self,
        title: str,
        description: str,
    ) -> AnalysisResult:

        prompt = self.prompt_builder.build_memory_prompt(
            title=title,
            description=description,
        )

        raw_response = self.client.generate(
            prompt,
        )

        print("\n========== RAW LLM RESPONSE ==========")
        print(raw_response)
        print("======================================\n")

        analysis = self.parser.parse(
            raw_response,
        )

        return analysis