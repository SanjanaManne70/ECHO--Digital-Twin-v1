from app.repositories.goal_repository import GoalRepository


class GoalPersistence:
    def __init__(self, goal_repo=None):
        self.goal_repo = goal_repo or GoalRepository()

    # Keep your existing save() method unchanged below this.
    def save(self, db, result, user_id=None, commit=True):
        """Apply validated goal updates for the specified user."""

        if result is None:
            return

        try:
            for update in result.goals:
                # Ignore low-confidence updates.
                if update.confidence < 0.6:
                    continue

                # Retrieve the goal with user scoping when provided.
                if user_id is None:
                    goal = self.goal_repo.get_by_id(
                        db,
                        update.goal_id,
                    )
                else:
                    goal = self.goal_repo.get_by_id(
                        db,
                        update.goal_id,
                        user_id=user_id,
                    )

                if goal is None:
                    continue

                # Update the current value without exceeding the target.
                goal.current_value = min(
                    goal.target_value,
                    goal.current_value + update.increment,
                )

                # Calculate progress percentage.
                if goal.target_value > 0:
                    goal.progress = min(
                        100,
                        int(
                            goal.current_value
                            / goal.target_value
                            * 100
                        ),
                    )
                else:
                    goal.progress = 0

                # Store the AI's explanation.
                goal.ai_reason = update.reason

                # Update completion state.
                if goal.current_value >= goal.target_value:
                    goal.current_value = goal.target_value
                    goal.progress = 100
                    goal.completed = True
                    goal.status = "completed"

            # Commit only when requested.
            if commit:
                db.commit()

        except Exception:
            db.rollback()
            raise
