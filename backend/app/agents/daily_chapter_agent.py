from app.prompts.daily_chapter_prompt import (
    DailyChapterPrompt,
)

from app.ai.daily_chapter_parser import (
    DailyChapterParser,
)

from app.llm.ollama_client import OllamaClient


class DailyChapterAgent:

    def __init__(self):

        self.prompt_builder = DailyChapterPrompt()

        self.client = OllamaClient()

        self.parser = DailyChapterParser()

    def generate(

        self,

        memories,

        insights,

        goals,

        current_state,

    ):

        prompt = self.prompt_builder.build(

            memories=memories,

            insights=insights,

            goals=goals,

            current_state=current_state,

        )

        raw_response = self.client.generate(

            prompt,

        )

        print("\n========== RAW DAILY CHAPTER ==========")

        print(raw_response)

        print("=======================================\n")

        return self.parser.parse(

            raw_response,

        )