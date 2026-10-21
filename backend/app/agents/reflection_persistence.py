from datetime import date

from app.models.reflection import Reflection
from app.repositories.reflection_repository import ReflectionRepository


class ReflectionPersistence:

    def __init__(self, repository=None):
        self.repository = repository or ReflectionRepository()

    def save(
        self,
        db,
        user_id,
        content,
    ):
        today = date.today()

        reflection = self.repository.get_by_date(
            db=db,
            user_id=user_id,
            day=today,
        )

        if reflection:

            reflection.content = content
            reflection.needs_refresh = False

            return self.repository.update(
                db,
                reflection,
            )

        reflection = Reflection(
            user_id=user_id,
            date=today,
            content=content,
            needs_refresh=False,
        )

        return self.repository.create(
            db,
            reflection,
        )