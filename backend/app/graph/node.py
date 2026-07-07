from datetime import datetime
from app.core.constants import (
    DEFAULT_LEARNING_RATE,
    MIN_NODE_VALUE,
    MAX_NODE_VALUE,
)

class Node:
    def __init__(
        self,
        name: str,
        current_value: float = 0,
        target_value: float = 0,
        confidence: float = 1.0,
    ):
        self.name = name
        self.current_value = current_value
        self.target_value = target_value
        self.confidence = confidence
        self.velocity = 0.0
        self.baseline_value = current_value
       
        self.pending_change= 0.0
        self.history = []

        self.last_updated = datetime.now()

    def update(self, value: float):
        self.history.append(self.current_value)

        self.current_value = value

        self.last_updated = datetime.now()

    def __repr__(self):

        return (
            f"{self.name}"
            f"(current={self.current_value}, "
            f"trend={self.trend()}, "
            f"confidence={self.confidence})"
        )
    def trend(self):

        if len(self.history) < 2:
            return "stable"

        if self.history[-1] > self.history[-2]:
            return "improving"

        elif self.history[-1] < self.history[-2]:
            return "declining"

        return "stable"
        
    def advance(self):

        # Calculate how far we are from the goal
        difference = (
            self.target_value
            - self.current_value
        )

        # Move a fraction towards the target
        self.velocity = (
            difference
            * self.learning_rate
        )

        self.current_value += self.velocity

        # Clamp between min and max
        if self.current_value > self.max_value:
            self.current_value = self.max_value

        if self.current_value < self.min_value:
            self.current_value = self.min_value

        self.current_value = round(
            self.current_value,
            2,
        )

        self.history.append(
            self.current_value
        )