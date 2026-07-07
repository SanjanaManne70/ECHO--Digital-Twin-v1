from app.ai.prompt_builder import PromptBuilder
from app.ai.response_parser import ResponseParser
from app.llm.ollama_client import OllamaClient
from app.simulation import result


class DecisionEngine:

    def __init__(self):

        self.prompt_builder = PromptBuilder()

        self.client = OllamaClient()

        self.parser = ResponseParser()

    def decide(

        self,

        analysis,

        goals,

        trend,

        memories,

        state,

    ):

        prompt = self.prompt_builder.build_decision_prompt(

            analysis=analysis,

            goals=goals,

            trend=trend,

            memories=memories,

            state=state,

        )

        raw = self.client.generate(prompt)

        print("\n========== DECISION LLM ==========\n")
        print(raw)
        print("\n==================================\n")

        result = self.parser.parse_decision(raw)

        print(result)

        return result
            

            
