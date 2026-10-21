from app.database.session import SessionLocal

from app.graph.graph_builder import GraphBuilder
from app.repositories.current_state_repository import CurrentStateRepository
from app.simulation.time_simulator import TimeSimulator
from app.simulation.habits import (
    GOOD_SLEEP,
    STUDY,
    EXERCISE,
)


db = SessionLocal()

repository = CurrentStateRepository()

states = repository.get_by_user(
    db,
    user_id=2,
)

graph = GraphBuilder().build(states)

simulator = TimeSimulator(graph)

result = simulator.simulate_days(
    days=30,
    actions=[
        GOOD_SLEEP,
        STUDY,
        EXERCISE,
    ],
)

for snapshot in result.snapshots:

    print(f"\n===== Day {snapshot.day} =====")

    for domain, value in snapshot.states.items():

        print(f"{domain}: {value}")

db.close()