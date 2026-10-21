from app.agents.context import AgentContext
from app.agents.trend_agent import TrendAgent


class FakeSnapshot:

    def __init__(self, sleep, energy, mood, learning):
        self.sleep = sleep
        self.energy = energy
        self.mood = mood
        self.learning = learning


def test_trend_agent_calculates_changes():

    snapshots = [
        FakeSnapshot(
            sleep=60,
            energy=70,
            mood=80,
            learning=90,
        ),
        FakeSnapshot(
            sleep=50,
            energy=60,
            mood=70,
            learning=80,
        ),
    ]

    context = AgentContext(
        snapshots=snapshots
    )

    agent = TrendAgent()

    result = agent.run(context)

    assert result.success is True
    assert result.agent_name == "trend"

    assert result.data["sleep_change"] == 10
    assert result.data["energy_change"] == 10
    assert result.data["mood_change"] == 10
    assert result.data["learning_change"] == 10

    assert context.trends == result.data


def test_trend_agent_handles_insufficient_history():

    context = AgentContext(
        snapshots=[
            FakeSnapshot(
                sleep=50,
                energy=50,
                mood=50,
                learning=50,
            )
        ]
    )

    agent = TrendAgent()

    result = agent.run(context)

    assert result.success is True
    assert result.data == {
        "summary": "Not enough history."
    }

    assert context.trends == result.data