from app.graph.node import Node
from app.graph.edge import Edge
from app.graph.alsg import ALSG

graph = ALSG()

sleep = Node(
    "Sleep",
    current_value=8,
    target_value=8,
)
sleep.history = [
    5,
    6,
    8,
]

energy = Node(
    "Energy",
    current_value=50,
    target_value=80,
)

mood = Node(
    "Mood",
    current_value=60,
    target_value=90,
)

learning = Node(
    "Learning",
    current_value=55,
    target_value=95,
)
graph.add_node(sleep)
graph.add_node(energy)
graph.add_node(mood)
graph.add_node(learning)

graph.add_edge(
    Edge(sleep, energy, 0.8)
)

graph.add_edge(
    Edge(energy, mood, 0.6)
)

graph.add_edge(
    Edge(mood, learning, 0.5)
)