from app.database.session import SessionLocal
from app.services.memory_service import MemoryService

db = SessionLocal()

service = MemoryService()

memory = service.remember(
    db=db,
    user_id=2,
    title="Solved Graph Algorithms",
    description="Completed graph propagation engine for ECHO.",
    domain="Learning",
    importance=0.9,
)

print(memory.id)
print(memory.title)

db.close()