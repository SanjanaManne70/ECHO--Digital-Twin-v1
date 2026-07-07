from app.agents.daily_chapter_agent import DailyChapterAgent
from app.ai.daily_chapter_parser import DailyChapterParser


class DailyChapterBuilder:

    def __init__(self):

        self.agent = DailyChapterAgent()

        self.parser = DailyChapterParser()

    def build(

        self,

        memories,

        insights,

        goals,

        current_state,

    ):

        raw = self.agent.generate(

            memories=memories,

            insights=insights,

            goals=goals,

            current_state=current_state,

        )

        return self.parser.parse(raw)