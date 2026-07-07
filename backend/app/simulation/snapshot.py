from dataclasses import dataclass


@dataclass
class SimulationSnapshot:

    day: int

    states: dict[str, float]