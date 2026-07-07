from app.graph.alsg import ALSG
from app.graph.node import Node
from app.graph.edge import Edge


class TwinService:

    def build_graph(
        self,
        current_state,
    ):

        graph = ALSG()

        nodes = {}

        for state in current_state:

            node = Node(
                name=state.domain,
                current_value=state.value,
                target_value=state.value,
            )

            nodes[state.domain] = node

            graph.add_node(node)

        return graph