from app.models.twin_snapshot import TwinSnapshot
from app.repositories.twin_snapshot_repository import (
    TwinSnapshotRepository,
)


class TwinSnapshotService:

    def __init__(self):

        self.repository = TwinSnapshotRepository()

    def save_snapshot(
        self,
        db,
        user_id,
        graph,
    ):

        snapshot = TwinSnapshot(

            user_id=user_id,

            sleep=graph.get_node("Sleep").current_value,

            energy=graph.get_node("Energy").current_value,

            mood=graph.get_node("Mood").current_value,

            learning=graph.get_node("Learning").current_value,

        )

        return self.repository.create(
            db,
            snapshot,
        )