from app.models.current_state import CurrentState


class GraphPersistence:

    def save(
        self,
        graph,
        states,
        db,
        user_id,
    ):

        lookup = {

            state.domain: state

            for state in states

        }

        for node in graph.nodes.values():

            if node.name in lookup:

                lookup[node.name].value = round(

                    node.current_value,

                    2,

                )

            else:

                db.add(

                    CurrentState(

                        user_id=user_id,

                        domain=node.name,

                        value=round(

                            node.current_value,

                            2,

                        ),

                    )

                )

        db.commit()