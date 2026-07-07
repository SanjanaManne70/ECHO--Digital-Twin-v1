from app.services.reflection_service import ReflectionService

class ReflectionHandler:

    def __init__(self):

        self.service = ReflectionService()

    def __call__(self, event):

        print("\n===== REFLECTION HANDLER =====")

        self.service.refresh_today(
            db=event.db,
            user_id=event.user_id,
        )

        print("Reflection refreshed.")
        print("=============================\n")