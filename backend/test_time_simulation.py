from app.graph.graph_data import graph
from app.simulation.time_simulator import TimeSimulator

simulator = TimeSimulator(graph)

future = simulator.simulate_days(30)

for node in future.nodes.values():
    print(node)