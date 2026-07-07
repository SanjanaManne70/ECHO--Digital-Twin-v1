from copy import deepcopy

from app.graph.alsg import ALSG


class Simulator:
    def __init__(self, graph: ALSG):
        self.graph = graph

    def simulate(self, node_name: str, new_value: float):
        simulation_graph = deepcopy(self.graph)

        node = simulation_graph.nodes[node_name]

        node.update(new_value)

        simulation_graph.propagate()

        return simulation_graph