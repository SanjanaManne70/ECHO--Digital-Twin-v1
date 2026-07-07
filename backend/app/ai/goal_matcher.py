from app.ai.prompt_builder import PromptBuilder
from app.ai.response_parser import ResponseParser
from app.llm.ollama_client import OllamaClient


class GoalMatcher:

    def __init__(self):

        self.prompt_builder = PromptBuilder()

        self.client = OllamaClient()

        self.parser = ResponseParser()

    def match(
         
            

        self,

        title,

        description,

        goals,

    ):
        print("Building Goal Prompt...")
        prompt = self.prompt_builder.build_goal_matching_prompt(

            title=title,

            description=description,

            goals=goals,

        )

        print("Calling Goal LLM...")
        raw = self.client.generate(

            prompt,

        )


        print("\n======= GOAL MATCHER =======")

        print(raw)

        print("============================\n")

        return self.parser.parse_goal_matching(

            raw,

        )
        print("Goal LLM Finished.")