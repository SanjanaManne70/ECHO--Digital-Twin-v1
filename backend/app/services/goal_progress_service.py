from app.ai.goal_matcher import GoalMatcher
from app.repositories.goal_repository import GoalRepository
from app.repositories.memory_repository import MemoryRepository


class GoalProgressService:

    def __init__(self):

        self.goal_repo = GoalRepository()

        self.memory_repo = MemoryRepository()

        self.matcher = GoalMatcher()

    def process_memory(
        self,
        db,
        user_id,
        memory_id,
    ):

        memory = self.memory_repo.get_by_id(

            db,

            memory_id,

        )

        if memory is None:

            return

        goals = self.goal_repo.get_all(

            db=db,

            user_id=user_id,

        )

        if not goals:

            return

        goal_payload = []

        for goal in goals:

            goal_payload.append({

                "goal_id": goal.id,

                "title": goal.title,

                "description": goal.description,

                "category": goal.category,

                "target_value": goal.target_value,

                "target_unit": goal.target_unit,

                "current_value": goal.current_value,

            })

        matches = self.matcher.match(

            title=memory.title,

            description=memory.description,

            goals=goal_payload,

        )

        for update in matches.updates:

            goal = self.goal_repo.get_by_id(

                db,

                update.goal_id,

            )

            if goal is None:

                continue

            if update.confidence < 0.6:

                continue

            goal.current_value += update.increment

            goal.progress = min(

                100,

                round(

                    goal.current_value

                    / goal.target_value

                    * 100,

                    2,

                ),

            )

            goal.ai_reason = update.reason

        db.commit()