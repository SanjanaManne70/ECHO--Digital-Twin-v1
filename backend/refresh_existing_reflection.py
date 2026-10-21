
from sqlalchemy import func

from app.database.session import SessionLocal
from app.models.memory_event import MemoryEvent
from app.agents.agent_context_loader import AgentContextLoader
from app.agents.reflection_agent import ReflectionAgent
from app.agents.reflection_persistence import ReflectionPersistence


def main():
    db = SessionLocal()

    try:
        users = (
            db.query(
                MemoryEvent.user_id,
                func.count(MemoryEvent.id).label("memory_count"),
            )
            .group_by(MemoryEvent.user_id)
            .order_by(MemoryEvent.user_id)
            .all()
        )

        if not users:
            print("No saved memories found.")
            return

        print("\nExisting memory owners:")
        for user_id, count in users:
            print(f"User ID: {user_id} | Memories: {count}")

        selected_id = int(input("\nEnter the user ID to refresh: "))

        if selected_id not in {uid for uid, _ in users}:
            print("Invalid user ID. No changes made.")
            return

        if input("Generate a new reflection? (yes/no): ").strip().lower() != "yes":
            print("Cancelled.")
            return

        context = AgentContextLoader().load(
            db=db,
            user_id=selected_id,
        )

        if not context.recent_memories:
            print("No recent memories found.")
            return

        print(
            f"\nRunning LLM with {len(context.recent_memories)} memories "
            f"and {len(context.snapshots)} snapshots..."
        )

        result = ReflectionAgent().run(context)

        if not result.success:
            print("Reflection generation failed:", result.errors)
            return

        print("\n========== GENERATED REFLECTION ==========\n")
        print(result.data)
        print("\n==========================================\n")

        if input("Save this reflection? (yes/no): ").strip().lower() != "yes":
            print("Generated only; nothing saved.")
            return

        ReflectionPersistence().save(
            db=db,
            user_id=selected_id,
            content=result.data,
        )

        print("Reflection refreshed successfully.")

    except Exception as exc:
        db.rollback()
        print(f"Refresh failed: {type(exc).__name__}: {exc}")

    finally:
        db.close()


if __name__ == "__main__":
    main()
