from app.repositories.daily_chapter_repository import (
    DailyChapterRepository,
)

from app.services.daily_chapter_service import (
    DailyChapterService,
)


class TimelineService:

    def __init__(self):

        self.chapter_repo = DailyChapterRepository()

        self.chapter_service = DailyChapterService()

    def get_timeline(
        self,
        db,
        user_id,
    ):

        chapters = self.chapter_repo.get_all(
            db=db,
            user_id=user_id,
        )

        timeline = []

        for chapter in chapters:

            if chapter.needs_refresh:

                chapter = self.chapter_service.refresh_day(
                    db=db,
                    user_id=user_id,
                    day=chapter.date,
                )

                # Safety check
                if chapter is None:
                    continue

            timeline.append({

                "date": chapter.date,

                "title": chapter.title,

                "mood": chapter.mood,

                "summary": chapter.summary,

                "growth": chapter.growth,

                "highlight": chapter.highlight,

                "tomorrow_focus": chapter.tomorrow_focus,

            })

        return timeline