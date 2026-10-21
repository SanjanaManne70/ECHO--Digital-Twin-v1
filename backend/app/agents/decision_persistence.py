from app.models.insight import Insight
from app.models.planner_task import PlannerTask

from app.repositories.insight_repository import InsightRepository
from app.repositories.planner_repository import PlannerRepository


class DecisionPersistence:

    def __init__(
        self,
        insight_repo=None,
        planner_repo=None,
    ):
        self.insight_repo = (
            insight_repo
            or InsightRepository()
        )

        self.planner_repo = (
            planner_repo
            or PlannerRepository()
        )

    def save(self, db, user_id, result, commit: bool = True):
        if result is None:
            return

        if result.insight:
            insight = Insight(
                user_id=user_id,
                title=result.insight.title,
                description=result.insight.description,
                severity=result.insight.severity,
            )
            self.insight_repo.create(db, insight, commit=False)

        if result.planner and result.planner.title:
            planner = PlannerTask(
                user_id=user_id,
                title=result.planner.title,
                description=result.planner.description,
                priority=result.planner.priority,
                completed=False,
            )
            self.planner_repo.create(db, planner, commit=False)

        if commit:
            db.commit()