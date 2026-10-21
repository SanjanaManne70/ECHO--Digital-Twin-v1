from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.api import (
    memory,
    current_state,
    simulation,
    reflection,
    planner,
    trend,
    insight,
    timeline,
    goal,
)

from app.core.config import settings

from app.events.event_bus import event_bus
from app.events.events import MemoryProcessedEvent
from app.events.coordinator_handler import CoordinatorHandler
from app.events.daily_chapter_handler import DailyChapterHandler

from app.agents.coordinator import Coordinator
from app.agents.registry import AgentRegistry
from app.agents.twin_agent import TwinAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.reflection_agent import ReflectionAgent
from app.agents.trend_agent import TrendAgent
from app.api import (
    memory,
    current_state,
    simulation,
    reflection,
    planner,
    trend,
    insight,
    timeline,
    goal,
    execution_history,
)
from app.api import execution_history
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


# ============================================================
# V2 AGENT REGISTRY
# ============================================================

agent_registry = AgentRegistry()

agent_registry.register(
    TwinAgent()
)

agent_registry.register(
    DecisionAgent()
)

agent_registry.register(
    ReflectionAgent()
)

agent_registry.register(
    TrendAgent()
)

# ============================================================
# V2 COORDINATOR
# ============================================================

coordinator = Coordinator(
    registry=agent_registry,
)


coordinator_handler = CoordinatorHandler(
    coordinator=coordinator,
)


# ============================================================
# EVENT SUBSCRIPTIONS
# ============================================================

# V2 Coordinator is now the single owner of:
#
# Twin
# Decision
# Insight
# Planner
# Goal
# Reflection
#
event_bus.subscribe(
    MemoryProcessedEvent,
    coordinator_handler,
)


# Daily chapter remains a separate deterministic
# bookkeeping handler for now.
event_bus.subscribe(
    MemoryProcessedEvent,
    DailyChapterHandler(),
)


# ============================================================
# CORS
# ============================================================

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# ROUTERS
# ============================================================

app.include_router(
    api_router
)

app.include_router(
    memory.router
)

app.include_router(
    current_state.router
)

app.include_router(
    simulation.router
)

app.include_router(
    reflection.router
)

app.include_router(
    planner.router
)

app.include_router(
    trend.router
)

app.include_router(
    insight.router
)

app.include_router(
    timeline.router
)

app.include_router(
    goal.router
)
app.include_router(
    execution_history.router
)