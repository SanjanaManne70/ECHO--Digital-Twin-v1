from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.services.current_state_service import (
    CurrentStateService,
)

class UserService:

    def __init__(self):
        self.repository = UserRepository()
        self.current_state_service = CurrentStateService()

    def register_user(
        self,
        db: Session,
        user_data: UserCreate,
    ):

        existing_user = self.repository.get_by_email(
            db,
            user_data.email,
        )

        if existing_user:
            raise ValueError(
                "Email already registered."
            )

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=hash_password(
                user_data.password
            ),
        )

        user = self.repository.create(
            db,
            user,
        )

        self.current_state_service.initialize(
            db=db,
            user_id=user.id,
        )

        return user

    def authenticate_user(
        self,
        db: Session,
        email: str,
        password: str,
    ):

        user = self.repository.get_by_email(
            db,
            email,
        )

        if not user or not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError(
                "Invalid email or password."
            )

        return user
