from datetime import date

from app.models.reflection import Reflection


class ReflectionRepository:

    def get_by_date(
        self,
        db,
        user_id,
        day,
    ):
        return (
            db.query(Reflection)
            .filter(
                Reflection.user_id == user_id,
                Reflection.date == day,
            )
            .first()
        )

    def get_latest(
        self,
        db,
        user_id,
    ):
        return (
            db.query(Reflection)
            .filter(
                Reflection.user_id == user_id,
            )
            .order_by(
                Reflection.date.desc()
            )
            .first()
        )

    def create(
        self,
        db,
        reflection,
    ):
        db.add(reflection)
        db.commit()
        db.refresh(reflection)
        return reflection

    def update(
        self,
        db,
        reflection,
    ):
        db.commit()
        db.refresh(reflection)
        return reflection

    def mark_dirty(
        self,
        db,
        user_id,
        day,
    ):
        reflection = self.get_by_date(
            db=db,
            user_id=user_id,
            day=day,
        )

        if reflection:

            reflection.needs_refresh = True

            db.commit()
            db.refresh(reflection)

            return reflection

        reflection = Reflection(
            user_id=user_id,
            date=day,
            content="",
            needs_refresh=True,
        )

        db.add(reflection)
        db.commit()
        db.refresh(reflection)

        return reflection