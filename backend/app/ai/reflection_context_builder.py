from app.repositories.current_state_repository import (
    CurrentStateRepository,
)

from app.repositories.memory_repository import (
    MemoryRepository,
)

from app.repositories.twin_snapshot_repository import (
    TwinSnapshotRepository,
)
from app.ai.trend_analyzer import TrendAnalyzer


class ReflectionContextBuilder:

    def __init__(self):

        self.current_repo = CurrentStateRepository()

        self.memory_repo = MemoryRepository()

        self.snapshot_repo = TwinSnapshotRepository()
        self.trend_analyzer = TrendAnalyzer()

    def build(
        self,
        db,
        user_id,
    ):

        current = self.current_repo.get_by_user(
            db,
            user_id,
        )
        

        memories = self.memory_repo.get_recent(
            db,
            user_id,
            limit=10,
        )

        snapshots = self.snapshot_repo.get_history(
            db,
            user_id,
            limit=30,
        )
        print("\n===== SNAPSHOT COUNT =====")
        print(len(snapshots))

        for s in snapshots:
            print(
                s.created_at,
                s.sleep,
                s.energy,
                s.mood,
                s.learning,
            )

        print("==========================\n")
        trend = self.trend_analyzer.analyze(
            snapshots,
        )
        print("\n===== TREND =====")
        print(trend)
        print("=================\n")
        return {

            "current": current,

            "memories": memories,

            "snapshots": snapshots,
    
            "trend": trend,

        }