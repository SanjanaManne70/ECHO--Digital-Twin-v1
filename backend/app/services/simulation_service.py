from app.ai.simulation_engine import SimulationEngine

from app.repositories.current_state_repository import CurrentStateRepository
from app.repositories.goal_repository import GoalRepository


class SimulationService:

    def __init__(self):

        self.engine = SimulationEngine()

        self.state_repo = CurrentStateRepository()

        self.goal_repo = GoalRepository()

    def simulate(

        self,

        db,

        user_id,

        scenario,

    ):

        state = self.state_repo.get_by_user(
            db=db,
            user_id=user_id,
        )

        goals = self.goal_repo.get_all(

            db=db,

            user_id=user_id,

        )

        current_state = []

        for s in state:

            current_state.append({

                "name": s.domain,

                "current": s.value,

            })

        goal_context = []

        for g in goals:

            goal_context.append({

                "id": g.id,

                "title": g.title,

                "current_progress": g.progress,

                "target_value": g.target_value,

                "target_unit": g.target_unit,

            })

        return self.engine.simulate(

            scenario=scenario,

            current_state=current_state,

            goals=goal_context,

        )