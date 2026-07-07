from app.graph.graph_data import graph
from app.simulation.simulator import Simulator

simulator = Simulator(graph)

future = simulator.simulate(
    "Sleep",
    9,
)

print("========== CURRENT ==========")

for node in graph.nodes.values():
    print(node)

print()

print("========== FUTURE ==========")

for node in future.nodes.values():
    print(node)