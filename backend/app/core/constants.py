# =====================================================
# Simulation
# =====================================================

DEFAULT_SIMULATION_DAYS = 30

MIN_NODE_VALUE = 0

MAX_NODE_VALUE = 100

DEFAULT_LEARNING_RATE = 0.20


# =====================================================
# Domain Names
# =====================================================

SLEEP = "Sleep"

ENERGY = "Energy"

MOOD = "Mood"

LEARNING = "Learning"


# =====================================================
# Graph Edge Weights
# =====================================================

SLEEP_TO_ENERGY = 0.80

ENERGY_TO_MOOD = 0.60

MOOD_TO_LEARNING = 0.50


# =====================================================
# Planner Target Values
# =====================================================

TARGET_VALUES = {
    SLEEP: 8,
    ENERGY: 90,
    MOOD: 95,
    LEARNING: 90,
}