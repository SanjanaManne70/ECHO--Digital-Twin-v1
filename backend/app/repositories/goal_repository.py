from sqlalchemy.orm import Session

from app.models.goal import Goal


class GoalRepository:

    def create(
        self,
        db: Session,
        goal: Goal,
    ):

        db.add(goal)
        db.commit()
        db.refresh(goal)

        return goal

    def get_all(
        self,
        db: Session,
        user_id: int,
    ):

        return (
            db.query(Goal)
            .filter(
                Goal.user_id == user_id,
            )
            .order_by(
                Goal.created_at.desc(),
            )
            .all()
        )

    def update(self, db: Session, goal: Goal, commit: bool = True):
        if commit:
            db.commit()
            db.refresh(goal)

        return goal

        return goal
    def delete(
        self,
        db: Session,
        goal: Goal,
    ):

        db.delete(goal)
        db.commit()

    
    def get_by_id(self, db, goal_id, user_id=None):
        query = db.query(Goal).filter(Goal.id == goal_id)

        if user_id is not None:
            query = query.filter(Goal.user_id == user_id)

        return query.first()
