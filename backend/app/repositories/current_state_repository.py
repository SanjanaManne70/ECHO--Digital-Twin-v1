from sqlalchemy.orm import Session

from app.models.current_state import CurrentState


class CurrentStateRepository:

    def get_by_user(
        self,
        db: Session,
        user_id: int,
    ):
        return (
            db.query(CurrentState)
            .filter(
                CurrentState.user_id == user_id
            )
            .all()
        )

    def get_all(
        self,
        db: Session,
        user_id: int,
    ):
        return self.get_by_user(
            db=db,
            user_id=user_id,
        )