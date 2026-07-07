from app.database.session import SessionLocal
from app.services.twin_update_service import TwinUpdateService

db = SessionLocal()

service = TwinUpdateService()

service.apply_memory(
    db=db,
    user_id=2,
    domain="Learning",
)

print("Twin updated successfully!")

db.close()