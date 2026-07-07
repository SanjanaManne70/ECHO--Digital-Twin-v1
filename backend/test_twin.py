from app.database.session import SessionLocal
from app.repositories.current_state_repository import CurrentStateRepository
from app.services.twin_service import TwinService

db = SessionLocal()

repo = CurrentStateRepository()
service = TwinService()

states = repo.get_by_user(db, 2)

graph = service.build_graph(states)

print("Nodes in Digital Twin:\n")

for node in graph.nodes.values():
    print(node)

db.close()