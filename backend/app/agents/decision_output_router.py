
from app.agents.decision_persistence import DecisionPersistence
from app.agents.goal_persistence import GoalPersistence


class DecisionOutputRouter:
    def __init__(self, decision_persistence=None, goal_persistence=None):
        self.decision_persistence = (
            decision_persistence or DecisionPersistence()
        )
        self.goal_persistence = (
            goal_persistence or GoalPersistence()
        )

    def persist(self, db, user_id, result):
        if result is None:
            return

        try:
            self.decision_persistence.save(
                db=db,
                user_id=user_id,
                result=result,
                commit=False,
            )

            self.goal_persistence.save(
                db=db,
                user_id=user_id,
                result=result,
                commit=False,
            )

            # Commit all decision-related changes together.
            db.commit()

        except Exception:
            db.rollback()
            raise
