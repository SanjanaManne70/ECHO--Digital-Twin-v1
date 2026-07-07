from datetime import date

from app.agents.daily_chapter_agent import DailyChapterAgent
from app.models.daily_chapter import DailyChapter

from app.repositories.daily_chapter_repository import DailyChapterRepository
from app.repositories.memory_repository import MemoryRepository
from app.repositories.insight_repository import InsightRepository
from app.repositories.current_state_repository import CurrentStateRepository


class DailyChapterService:

    def __init__(self):

        self.agent = DailyChapterAgent()

        self.chapter_repo = DailyChapterRepository()

        self.memory_repo = MemoryRepository()

        self.insight_repo = InsightRepository()


        self.state_repo = CurrentStateRepository()

    def refresh_day(
        self,
        db,
        user_id,
        day,
    ):

        today = day

        memories = self.memory_repo.get_by_day(
            db=db,
            user_id=user_id,
            day=day,
        )

        # Nothing happened today
        if not memories:

            existing = self.chapter_repo.get_by_date(
                db=db,
                user_id=user_id,
                date=day,
            )

            if existing:
                existing.needs_refresh = False
                return self.chapter_repo.update(db, existing)

            return None

        insights = self.insight_repo.get_recent(
            db=db,
            user_id=user_id,
            limit=5,
        )

       
        state = self.state_repo.get_by_user(
            db=db,
            user_id=user_id,
        )

        # -----------------------------
        # Convert ORM objects -> dicts
        # -----------------------------

        memories_context = [

            {
                "title": memory.title,
                "description": memory.description,
            }

            for memory in memories

        ]

        insights_context = [

            {
                "title": insight.title,
                "description": insight.description,
            }

            for insight in insights

        ]
        goals_context = []

        state_context = [

            {
                "domain": item.domain,
                "value": item.value,
            }

            for item in state

        ]

        # -----------------------------
        # Generate AI chapter
        # -----------------------------

        chapter = self.agent.generate(

            memories=memories_context,

            insights=insights_context,

            goals=goals_context,

            current_state=state_context,

        )

        existing = self.chapter_repo.get_by_date(

            db=db,

            user_id=user_id,

            date=day,

        )

        if existing:

            existing.title = chapter["title"]
            existing.mood = chapter["mood"]
            existing.summary = chapter["summary"]
            existing.growth = chapter["growth"]
            existing.highlight = chapter["highlight"]
            existing.tomorrow_focus = chapter["tomorrow"]
            existing.needs_refresh = False

            return self.chapter_repo.update(

                db,

                existing,

            )

        new = DailyChapter(

            user_id=user_id,

            date=day,

            title=chapter["title"],

            mood=chapter["mood"],

            summary=chapter["summary"],

            growth=chapter["growth"],

            highlight=chapter["highlight"],

            tomorrow_focus=chapter["tomorrow"],
            needs_refresh=False,


        )

        return self.chapter_repo.create(

            db,

            new,

        )
    