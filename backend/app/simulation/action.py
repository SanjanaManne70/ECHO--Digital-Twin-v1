from dataclasses import dataclass


@dataclass
class Action:
    domain: str
    delta: float