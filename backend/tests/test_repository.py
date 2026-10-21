from app.database.session import SessionLocal
from app.repositories.current_state_repository import CurrentStateRepository

db = SessionLocal()

repo = CurrentStateRepository()

states = repo.get_by_user(db, 2)

for state in states:
    print(state.domain, state.value)

db.close()