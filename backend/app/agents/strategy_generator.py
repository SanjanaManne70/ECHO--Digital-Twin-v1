from app.agents.planner_models import (
    Goal,
    Strategy,
)

from app.agents.habit_library import (
    GOOD_SLEEP,
    EXERCISE,
    STUDY,
    MEDITATION,
    READING,
)


class StrategyGenerator:

    def generate(
        self,
        goal: Goal,
    ) -> Strategy:

        habits = []

        text = (
            goal.title
            + " "
            + goal.description
        ).lower()

        # Sleep
        if any(word in text for word in [
            "sleep",
            "rest",
            "tired",
        ]):
            habits.append(GOOD_SLEEP)

        # Exercise
        if any(word in text for word in [
            "exercise",
            "gym",
            "fitness",
            "workout",
            "health",
        ]):
            habits.append(EXERCISE)

        # Learning
        if any(word in text for word in [
            "study",
            "learn",
            "placement",
            "interview",
            "coding",
            "google",
            "career",
        ]):
            habits.append(STUDY)

        # Reading
        if any(word in text for word in [
            "read",
            "books",
            "knowledge",
        ]):
            habits.append(READING)

        # Meditation
        if any(word in text for word in [
            "stress",
            "calm",
            "anxiety",
            "focus",
            "meditation",
        ]):
            habits.append(MEDITATION)

        return Strategy(
            goal=goal,
            habits=habits,
            reasoning="Strategy generated from user goal.",
            expected_outcome="Improvement in the target life domains.",
        )