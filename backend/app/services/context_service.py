from app.repositories.current_state_repository import (
    CurrentStateRepository,
)
from app.repositories.memory_repository import (
    MemoryRepository,
)
from app.agents.context_builder import ContextBuilder


class ContextService:

    def __init__(self):

        self.state_repo = CurrentStateRepository()
        self.memory_repo = MemoryRepository()
        self.builder = ContextBuilder()

    def get_context(
        self,
        db,
        user_id,
    ):

        states = self.state_repo.get_by_user(
            db,
            user_id,
        )

        memories = self.memory_repo.latest_memories(
            db,
            user_id,
        )

        return self.builder.build(
            states,
            memories,
        )