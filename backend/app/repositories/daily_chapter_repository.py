from datetime import date

from app.models.daily_chapter import DailyChapter


class DailyChapterRepository:

    def get_by_date(
        self,
        db,
        user_id,
        date,
    ):

        return (
            db.query(DailyChapter)
            .filter(
                DailyChapter.user_id == user_id,
                DailyChapter.date == date,
            )
            .first()
        )

    def create(
        self,
        db,
        chapter,
    ):

        db.add(chapter)
        db.commit()
        db.refresh(chapter)

        return chapter

    def update(
        self,
        db,
        chapter,
    ):

        db.commit()
        db.refresh(chapter)

        return chapter

    def get_all(
        self,
        db,
        user_id,
    ):

        return (
            db.query(DailyChapter)
            .filter(
                DailyChapter.user_id == user_id,
            )
            .order_by(
                DailyChapter.date.desc()
            )
            .all()
        )

    def mark_dirty(
        self,
        db,
        user_id,
        day,
    ):

        chapter = self.get_by_date(
            db=db,
            user_id=user_id,
            date=day,
        )

        if chapter:

            chapter.needs_refresh = True

            db.commit()

            db.refresh(chapter)

            return chapter

        chapter = DailyChapter(

            user_id=user_id,

            date=day,

            title="",

            mood="🙂",

            summary="",

            growth=[],

            highlight="",

            tomorrow_focus="",

            needs_refresh=True,

        )

        db.add(chapter)

        db.commit()

        db.refresh(chapter)

        return chapter