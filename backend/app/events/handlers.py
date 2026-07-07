from app.events.events import MemoryProcessedEvent
from app.services.twin_update_service import TwinUpdateService
from app.services.insight_service import InsightService
from app.services.planner_service import PlannerService
from app.services.goal_progress_service import GoalProgressService
class TwinUpdateHandler:

    def __init__(self):

        self.service = TwinUpdateService()

    def __call__(
        self,
        event: MemoryProcessedEvent,
    ):

        print("\n===== EVENT RECEIVED =====")
        print("Updating Twin...")
        print("==========================\n")

        self.service.apply_memory(
            db=event.db,
            user_id=event.user_id,
            analysis=event.analysis,
        )

class InsightHandler:

    def __init__(self):

        self.service = InsightService()

    def __call__(
        self,
        event,
    ):

        print("\n===== EVENT RECEIVED =====")
        print("Generating Insight...")
        print("==========================\n")

        self.service.generate(

            db=event.db,

            user_id=event.user_id,

            analysis=event.analysis,

        )

class PlannerHandler:

    def __init__(self):

        self.service = PlannerService()

    def __call__(
        self,
        event,
    ):

        print("\n===== PLANNER =====")

        self.service.generate(
            db=event.db,
            user_id=event.user_id,
            analysis=event.analysis,
        )

        print("Planner Saved")

        print("===================\n")

class GoalProgressHandler:

    def __init__(self):

        self.service = GoalProgressService()

    def __call__(

        self,

        event,

    ):

        print("\n===== GOAL PROGRESS =====")

        self.service.process_memory(

            db=event.db,

            user_id=event.user_id,

            memory_id=event.memory_id,

        )

        print("Goals Updated")

        print("=========================\n")