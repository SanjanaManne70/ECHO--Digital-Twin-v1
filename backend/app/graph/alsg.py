from app.graph.node import Node
from app.graph.edge import Edge


class ALSG:

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node: Node):
        self.nodes[node.name] = node

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def propagate(self, steps=3):

        for _ in range(steps):

            # Reset pending changes
            for node in self.nodes.values():
                node.pending_change = 0

            # Collect influences
            for edge in self.edges:

                delta = (
                    edge.source.current_value
                    - edge.source.baseline_value
                )

                influence = (
                    delta
                    * edge.weight
                    * edge.confidence
                )

                edge.target.pending_change += influence

            # Apply influences
            for node in self.nodes.values():

                if node.pending_change != 0:

                    new_value = (
                        node.current_value
                        + node.pending_change
                    )

                    new_value = max(
                        0,
                        min(
                            100,
                            new_value,
                        ),
                    )

                    node.update(
                        new_value
                    )
        # IMPORTANT:
        # After propagation, make the current state the new baseline
        for node in self.nodes.values():
            node.baseline_value = node.current_value

    def get_node(
        self,
        name: str,
    ):
        return self.nodes.get(name)

    def apply_change(
        self,
        node_name,
        amount,
    ):

        node = self.get_node(node_name)

        if node:

            new_value = node.current_value + amount

            # Keep values between 0 and 100
            new_value = max(0, min(100, new_value))

            node.update(new_value)