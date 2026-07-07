from app.graph.alsg import ALSG
from app.graph.node import Node
from app.graph.edge import Edge
from app.core.constants import (
    TARGET_VALUES,
    SLEEP,
    ENERGY,
    MOOD,
    LEARNING,
    SLEEP_TO_ENERGY,
    ENERGY_TO_MOOD,
    MOOD_TO_LEARNING,
)


class GraphBuilder:

    DEFAULT_VALUE = 50

    def build(
        self,
        states,
    ):

        graph = ALSG()
        lookup = {}

        # ----------------------------
        # First-time user
        # ----------------------------

        if not states:

            for domain in [

                SLEEP,

                ENERGY,

                MOOD,

                LEARNING,

            ]:

                node = Node(

                    name=domain,

                    current_value=self.DEFAULT_VALUE,

                    target_value=TARGET_VALUES.get(
                        domain,
                        self.DEFAULT_VALUE,
                    ),

                )

                graph.add_node(node)

                lookup[domain] = node

        else:

            for state in states:

                node = Node(

                    name=state.domain,

                    current_value=state.value,

                    target_value=TARGET_VALUES.get(
                        state.domain,
                        state.value,
                    ),

                )

                graph.add_node(node)

                lookup[state.domain] = node

        # ----------------------------
        # Add edges
        # ----------------------------

        if SLEEP in lookup and ENERGY in lookup:

            graph.add_edge(
                Edge(
                    lookup[SLEEP],
                    lookup[ENERGY],
                    SLEEP_TO_ENERGY,
                )
            )

        if ENERGY in lookup and MOOD in lookup:

            graph.add_edge(
                Edge(
                    lookup[ENERGY],
                    lookup[MOOD],
                    ENERGY_TO_MOOD,
                )
            )

        if MOOD in lookup and LEARNING in lookup:

            graph.add_edge(
                Edge(
                    lookup[MOOD],
                    lookup[LEARNING],
                    MOOD_TO_LEARNING,
                )
            )

        return graph