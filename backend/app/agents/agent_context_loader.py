from app.ai.trend_analyzer import TrendAnalyzer

from app.repositories.current_state_repository import CurrentStateRepository
from app.repositories.goal_repository import GoalRepository
from app.repositories.memory_repository import MemoryRepository
from app.repositories.twin_snapshot_repository import TwinSnapshotRepository

from .context import AgentContext


class AgentContextLoader:

    def __init__(
        self,
        current_state_repository=None,
        goal_repository=None,
        memory_repository=None,
        snapshot_repository=None,
        trend_analyzer=None,
    ):

        self.current_state_repository = (
            current_state_repository
            or CurrentStateRepository()
        )

        self.goal_repository = (
            goal_repository
            or GoalRepository()
        )

        self.memory_repository = (
            memory_repository
            or MemoryRepository()
        )

        self.snapshot_repository = (
            snapshot_repository
            or TwinSnapshotRepository()
        )

        self.trend_analyzer = (
            trend_analyzer
            or TrendAnalyzer()
        )

    def load(
        self,
        db,
        user_id,
        memory_analysis=None,
        memory_id=None,
    ) -> AgentContext:

        current_state = (
            self.current_state_repository.get_by_user(
                db=db,
                user_id=user_id,
            )
        )

        goals = (
            self.goal_repository.get_all(
                db=db,
                user_id=user_id,
            )
        )

        recent_memories = (
            self.memory_repository.get_recent(
                db=db,
                user_id=user_id,
                limit=10,
            )
        )

        snapshots = (
            self.snapshot_repository.get_history(
                db=db,
                user_id=user_id,
                limit=30,
            )
        )

        trends = self.trend_analyzer.analyze(
            snapshots=snapshots,
        )

        return AgentContext(
            db=db,
            user_id=user_id,
            current_state=current_state,
            recent_memories=recent_memories,
            memory_analysis=memory_analysis,
            goals=goals,
            snapshots=snapshots,
            trends=trends,
            metadata={
                "memory_id": memory_id,
            },
        )
    
    def refresh(
        self,
        context: AgentContext,
    ) -> AgentContext:
        """
        Refresh mutable user data inside the existing AgentContext.
        """

        if context.db is None or context.user_id is None:
            return context

        current_state = (
            self.current_state_repository.get_by_user(
                db=context.db,
                user_id=context.user_id,
            )
        )

        goals = (
            self.goal_repository.get_all(
                db=context.db,
                user_id=context.user_id,
            )
        )

        recent_memories = (
            self.memory_repository.get_recent(
                db=context.db,
                user_id=context.user_id,
                limit=10,
            )
        )

        snapshots = (
            self.snapshot_repository.get_history(
                db=context.db,
                user_id=context.user_id,
                limit=30,
            )
        )

        trends = self.trend_analyzer.analyze(
            snapshots=snapshots,
        )

        context.current_state = current_state
        context.goals = goals
        context.recent_memories = recent_memories
        context.snapshots = snapshots
        context.trends = trends

        return context