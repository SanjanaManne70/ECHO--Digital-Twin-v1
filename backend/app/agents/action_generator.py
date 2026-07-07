from app.agents.planner_models import Strategy
from app.simulation.action import Action


class ActionGenerator:

    def generate(
        self,
        strategy: Strategy,
    ) -> list[Action]:

        actions = []

        for habit in strategy.habits:

            for domain, delta in habit.impacts.items():

                actions.append(
                    Action(
                        domain=domain,
                        delta=delta,
                    )
                )

        return actions