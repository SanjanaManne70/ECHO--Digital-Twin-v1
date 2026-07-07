from app.agents.planner_models import Habit


GOOD_SLEEP = Habit(
    name="Sleep 8 Hours",
    description="Maintain a consistent sleep schedule.",
    estimated_minutes=480,
    impacts={
        "Sleep": 0.30,
        "Energy": 0.15,
    },
)

EXERCISE = Habit(
    name="Exercise",
    description="Exercise for at least 30 minutes.",
    estimated_minutes=30,
    impacts={
        "Energy": 0.25,
        "Mood": 0.15,
    },
)

STUDY = Habit(
    name="Focused Study",
    description="Practice deep work without distractions.",
    estimated_minutes=120,
    impacts={
        "Learning": 0.25,
    },
)

MEDITATION = Habit(
    name="Meditation",
    description="Practice mindfulness.",
    estimated_minutes=20,
    impacts={
        "Mood": 0.20,
    },
)

READING = Habit(
    name="Reading",
    description="Read for personal growth.",
    estimated_minutes=30,
    impacts={
        "Learning": 0.10,
        "Mood": 0.05,
    },
)