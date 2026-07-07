from copy import deepcopy

from app.simulation.snapshot import SimulationSnapshot
from app.simulation.result import SimulationResult


class TimeSimulator:

    def __init__(self, graph):
        self.graph = graph

    def simulate_days(
        self,
        days: int,
        actions=None,
    ):

        graph = deepcopy(self.graph)

        snapshots = []

        if actions is None:
            actions = []

        for day in range(1, days + 1):

            # Apply user actions
            for action in actions:

                graph.apply_change(
                    action.domain,
                    action.delta,
                )

            # Natural progression
            for node in graph.nodes.values():
                node.advance()

            # Propagate effects
            graph.propagate()

            # Save snapshot
            snapshots.append(
                SimulationSnapshot(
                    day=day,
                    states={
                        node.name: round(
                            node.current_value,
                            2,
                        )
                        for node in graph.nodes.values()
                    },
                )
            )

        return SimulationResult(
            snapshots=snapshots,
        )