from app.graph.graph_builder import GraphBuilder
from app.graph.graph_persistence import GraphPersistence
from app.repositories.current_state_repository import CurrentStateRepository
from app.services.twin_snapshot_service import TwinSnapshotService
class TwinUpdateService:

    def __init__(self):

        self.repository = CurrentStateRepository()

        self.builder = GraphBuilder()

        self.persistence = GraphPersistence()

        self.snapshot_service = TwinSnapshotService()