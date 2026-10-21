from app.agents.agent_context_loader import AgentContextLoader
from app.ai.analysis_result import AnalysisResult


class FakeCurrentStateRepository:

    def get_by_user(self, db, user_id):
        return [
            {"domain": "Sleep", "value": 40},
            {"domain": "Energy", "value": 45},
        ]


class FakeGoalRepository:

    def get_all(self, db, user_id):
        return [
            {"title": "Study daily"},
        ]


class FakeMemoryRepository:

    def get_recent(self, db, user_id, limit=10):
        return [
            {"description": "Studied for two hours"},
        ]


class FakeSnapshotRepository:

    def get_history(self, db, user_id, limit=30):
        return [
            {"sleep": 45, "energy": 48, "mood": 52, "learning": 55},
            {"sleep": 50, "energy": 50, "mood": 50, "learning": 50},
        ]


class FakeTrendAnalyzer:

    def analyze(self, snapshots):
        return {
            "sleep_change": -5,
            "energy_change": -2,
            "mood_change": 2,
            "learning_change": 5,
        }


def test_agent_context_loader_loads_shared_context():

    loader = AgentContextLoader(
        current_state_repository=FakeCurrentStateRepository(),
        goal_repository=FakeGoalRepository(),
        memory_repository=FakeMemoryRepository(),
        snapshot_repository=FakeSnapshotRepository(),
        trend_analyzer=FakeTrendAnalyzer(),
    )

    analysis = AnalysisResult(
        emotion="tired",
        sentiment="negative",
        severity="medium",
        confidence=0.9,
        affected_domains=["Sleep"],
    )

    context = loader.load(
        db="fake-db",
        user_id=123,
        memory_analysis=analysis,
        memory_id=456,
    )

    assert context.db == "fake-db"
    assert context.user_id == 123

    assert context.memory_analysis == analysis

    assert len(context.current_state) == 2
    assert len(context.goals) == 1
    assert len(context.recent_memories) == 1
    assert len(context.snapshots) == 2

    assert context.trends["sleep_change"] == -5
    assert context.trends["learning_change"] == 5

    assert context.metadata["memory_id"] == 456