from app.repositories.current_state_repository import (
    CurrentStateRepository,
)

from app.graph.graph_builder import GraphBuilder
from app.graph.graph_persistence import GraphPersistence
from app.services.twin_snapshot_service import TwinSnapshotService

class TwinUpdateService:

    def __init__(self):

        self.repository = CurrentStateRepository()

        self.builder = GraphBuilder()

        self.persistence = GraphPersistence()
        self.snapshot_service = TwinSnapshotService()
    def apply_memory(
        self,
        db,
        user_id,
        analysis,
    ):

        # Load current state from DB
        states = self.repository.get_by_user(
            db,
            user_id,
        )

        # Build ALSG
        graph = self.builder.build(
            states,
        )

        severity_weight = {
            "low": 1,
            "medium": 3,
            "moderate": 3,
            "high": 5,
        }

        base = severity_weight.get(
            analysis.severity,
            1,
        )

        if analysis.sentiment == "negative":
            base *= -1

        print("\n===== INITIAL IMPACT =====")
        print("Domains:", analysis.affected_domains)
        print("Score:", base)
        print("==========================\n")

        # Apply initial impact
        for domain in analysis.affected_domains:

            graph.apply_change(
                domain,
                base,
            )

        # Propagate through ALSG
        graph.propagate()

        # Save updated graph back to DB
        self.persistence.save(

    graph=graph,

    states=states,

    db=db,

    user_id=user_id,

)
        self.snapshot_service.save_snapshot(
            db=db,
            user_id=user_id,
            graph=graph,
        )

        print("\n===== GRAPH UPDATED =====")

        for node in graph.nodes.values():
            print(
                node.name,
                "->",
                node.current_value,
            )

        print("=========================\n")