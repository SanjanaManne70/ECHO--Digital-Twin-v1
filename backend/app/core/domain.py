from enum import Enum


class Domain(str, Enum):

    SLEEP = "Sleep"

    ENERGY = "Energy"

    MOOD = "Mood"

    LEARNING = "Learning"