from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.api import memory
from app.api import current_state
from fastapi.middleware.cors import CORSMiddleware
from app.api import simulation
from app.events.event_bus import event_bus
from app.events.events import MemoryProcessedEvent
from app.events.handlers import TwinUpdateHandler
from app.events.decision_handler import DecisionHandler
from app.api import reflection
from app.api import planner
from app.api import trend
from app.api import insight
from app.api import timeline
from app.api import goal
from app.events.daily_chapter_handler import DailyChapterHandler
from app.events.reflection_handler import ReflectionHandler
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)
event_bus.subscribe(
    MemoryProcessedEvent,
    TwinUpdateHandler(),
)
event_bus.subscribe(
    MemoryProcessedEvent,
    DecisionHandler(),
)
event_bus.subscribe(
    MemoryProcessedEvent,
    DailyChapterHandler(),
)
event_bus.subscribe(
    MemoryProcessedEvent,
    ReflectionHandler(),
)

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

app.include_router(api_router)

app.include_router(memory.router)
app.include_router(current_state.router)
app.include_router(
    simulation.router
)
app.include_router(reflection.router)   
app.include_router(
    planner.router,
)
app.include_router(
    trend.router,
)

app.include_router(
    insight.router,
)
app.include_router(
    timeline.router,
)
app.include_router(goal.router)