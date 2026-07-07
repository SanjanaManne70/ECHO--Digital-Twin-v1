from datetime import date

from app.repositories.daily_chapter_repository import (
    DailyChapterRepository,
)


class DailyChapterHandler:

    def __init__(self):
        self.repo = DailyChapterRepository()

    def __call__(self, event):

        print("🔥 DailyChapterHandler triggered!")

        self.repo.mark_dirty(
            db=event.db,
            user_id=event.user_id,
            day=date.today(),
        )