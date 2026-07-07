from app.simulation.action import Action


GOOD_SLEEP = Action(
    domain="Sleep",
    delta=0.3,
)

STUDY = Action(
    domain="Learning",
    delta=0.2,
)

EXERCISE = Action(
    domain="Energy",
    delta=0.25,
)

MEDITATION = Action(
    domain="Mood",
    delta=0.15,
)