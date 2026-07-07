from app.graph.graph_data import graph

graph.propagate()

for node in graph.nodes.values():
    print(node)