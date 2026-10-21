
from uuid import uuid4

import pytest

from app.database.session import SessionLocal
from app.models.user import User
from app.services.memory_service import MemoryService
from app.events.event_bus import event_bus

from app.agents.coordinator import Coordinator
from app.agents.registry import AgentRegistry
from app.agents.twin_agent import TwinAgent
from app.agents.trend_agent import TrendAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.reflection_agent import ReflectionAgent
from app.events.coordinator_handler import CoordinatorHandler


def test_real_v2_event_flow(monkeypatch):
    registry = AgentRegistry()
    registry.register(TwinAgent())
    registry.register(TrendAgent())
    registry.register(DecisionAgent())
    registry.register(ReflectionAgent())

    coordinator = Coordinator(registry=registry)
    coordinator_handler = CoordinatorHandler(
        coordinator=coordinator
    )

    captured = {}

    def dispatch_test_event(event):
        captured["event"] = event
        captured["results"] = coordinator_handler(event)

    # Prevent unrelated production event subscribers from running.
    # The test explicitly dispatches its event to its local handler.
    monkeypatch.setattr(event_bus, "publish", dispatch_test_event)

    db = SessionLocal()
    user = None

    try:
        user = User(
            full_name="ECHO Integration Test",
            email=f"echo-test-{uuid4().hex}@example.invalid",
            password_hash="test-only-not-a-real-password",
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        service = MemoryService()
        memory = service.remember(
            db=db,
            user_id=user.id,
            title="V2 Multi Agent Integration Test",
            description=(
                "I completed a focused development session today. "
                "I want to track my progress, identify patterns, "
                "and plan the next steps for my project."
            ),
        )

        assert memory is not None
        assert memory.id is not None
        assert memory.user_id == user.id

        assert "event" in captured, (
            "MemoryService did not publish a memory event."
        )
        assert captured["event"].memory_id == memory.id
        assert captured["event"].user_id == user.id

        results = captured.get("results")
        assert results is not None, (
            "The coordinator handler did not return results."
        )

        expected_agents = {
            "twin",
            "trend",
            "decision",
            "reflection",
        }
        assert expected_agents.issubset(results.keys()), (
            f"Missing agent results. Received: {list(results.keys())}"
        )

        failures = {
            name: getattr(result, "error", None)
            for name, result in results.items()
            if not result.success
        }

        assert not failures, (
            f"One or more agents failed: {failures}"
        )

        print("\n========== REAL V2 EVENT FLOW ==========")
        print("Test user ID:", user.id)
        print("Memory ID:", memory.id)

        for name in (
            "twin",
            "trend",
            "decision",
            "reflection",
        ):
            result = results[name]
            print(f"{name}: success={result.success}")
            print(f"{name} output: {result.data}")

        print("REAL V2 FLOW COMPLETED SUCCESSFULLY")
        print("=======================================\n")

    finally:
        # The database is echo_test_db, not the production database.
        # Preserve the evidence for now if a failure needs debugging.
        db.close()
