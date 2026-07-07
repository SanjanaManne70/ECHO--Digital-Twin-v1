from app.ai.decision_engine import DecisionEngine

from app.repositories.insight_repository import InsightRepository
from app.repositories.planner_repository import PlannerRepository

from app.models.insight import Insight
from app.models.planner_task import PlannerTask


class DecisionHandler:

    def __init__(self):

        self.engine = DecisionEngine()

        self.insight_repo = InsightRepository()

        self.planner_repo = PlannerRepository()

    def __call__(self, event):

        print("\n========== DECISION ENGINE ==========\n")

        # We don't have Goals yet.
        # Send an empty list to the AI.
        goal_context = []

        print("\n===== GOALS SENT TO LLM =====")
        print(goal_context)
        print("=============================\n")

        result = self.engine.decide(
            analysis=event.analysis,
            goals=goal_context,
            trend=[],
            memories=[],
            state=[],
        )

        print("\n===== DECISION RESULT =====")
        print(result)
        print("===========================\n")

        # -----------------------------
        # Save Insight
        # -----------------------------
        if result.insight:

            insight = Insight(
                user_id=event.user_id,
                title=result.insight.title,
                description=result.insight.description,
                severity=result.insight.severity,
            )

            self.insight_repo.create(
                event.db,
                insight,
            )

        # -----------------------------
        # Save Planner Task
        # -----------------------------
        if result.planner and result.planner.title:

            planner = PlannerTask(
                user_id=event.user_id,
                title=result.planner.title,
                description=result.planner.description,
                priority=result.planner.priority,
                completed=False,
            )

            self.planner_repo.create(
                event.db,
                planner,
            )

        # -----------------------------
        # Goal updates are disabled
        # until the Goals module exists.
        # -----------------------------

        event.db.commit()

        print("\n===== DECISION COMPLETE =====\n")