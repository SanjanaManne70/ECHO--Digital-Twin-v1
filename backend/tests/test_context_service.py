from app.database.session import SessionLocal
from app.services.context_service import ContextService

db = SessionLocal()

service = ContextService()

context = service.get_context(
    db,
    user_id=2,
)

print(context)