from dataclasses import dataclass

from app.simulation.snapshot import SimulationSnapshot


@dataclass
class SimulationResult:

    snapshots: list[SimulationSnapshot]