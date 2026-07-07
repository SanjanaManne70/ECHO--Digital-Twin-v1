from app.models.goal import Goal
from app.repositories.goal_repository import GoalRepository


class GoalService:

    def __init__(self):
        self.repository = GoalRepository()

    def get_all(
        self,
        db,
        user_id,
    ):
        return self.repository.get_all(
            db=db,
            user_id=user_id,
        )

    def create(
        self,
        db,
        user_id,
        title,
        description,
    ):

        goal = Goal(
            user_id=user_id,

            title=title,
            description=description,

            category="General",
            target_value=100,
            target_unit="Points",

            current_value=0,
            progress=0,

            ai_reason="Analyzing your goal...",
            predicted_completion="Calculating...",

            completed=False,
        )

        return self.repository.create(
            db=db,
            goal=goal,
        )

    def delete(
        self,
        db,
        goal_id,
    ):

        goal = self.repository.get_by_id(
            db,
            goal_id,
        )

        if goal is None:
            return {
                "message": "Goal not found."
            }

        self.repository.delete(
            db,
            goal,
        )

        return {
            "message": "Goal deleted."
        }