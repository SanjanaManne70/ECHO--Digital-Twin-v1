from app.agents.agent_context_loader import AgentContextLoader
from app.agents.coordinator import Coordinator
from app.agents.decision_persistence import DecisionPersistence
from app.agents.goal_persistence import GoalPersistence
from app.agents.reflection_persistence import ReflectionPersistence
from app.events.events import MemoryProcessedEvent
from app.agents.workflows import DEFAULT_MEMORY_WORKFLOW
from app.agents.workflow import AgentStep
from app.agents.decision_output_router import DecisionOutputRouter
class CoordinatorHandler:

    def __init__(
        self,
        coordinator: Coordinator,
        context_loader: AgentContextLoader | None = None,
        decision_persistence: DecisionPersistence | None = None,
        goal_persistence: GoalPersistence | None = None,
        reflection_persistence: ReflectionPersistence | None = None,
        workflow: list[str | AgentStep] | None = None,
        decision_output_router: DecisionOutputRouter | None = None,
    ):
        self.coordinator = coordinator

        self.context_loader = (
            context_loader
            or AgentContextLoader()
        )

        self.decision_persistence = (
            decision_persistence
            or DecisionPersistence()
        )

        self.goal_persistence = (
            goal_persistence
            or GoalPersistence()
        )

        self.reflection_persistence = (
            reflection_persistence
            or ReflectionPersistence()
        )

        self.workflow = (
            workflow
            or DEFAULT_MEMORY_WORKFLOW
        )

        self.decision_output_router = (
            decision_output_router
            or DecisionOutputRouter(
                decision_persistence=self.decision_persistence,
                goal_persistence=self.goal_persistence,
            )
        )
    def __call__(
        self,
        event: MemoryProcessedEvent,
    ):

        # --------------------------------------------------
        # 1. Build shared AgentContext
        # --------------------------------------------------

        context = self.context_loader.load(
            db=event.db,
            user_id=event.user_id,
            memory_analysis=event.analysis,
            memory_id=event.memory_id,
        )

        # --------------------------------------------------
        # 2. Run multi-agent workflow
        # --------------------------------------------------

        results = self.coordinator.run(
            context=context,
            workflow=self.workflow,
        )

        # --------------------------------------------------
        # 3. Persist Decision output
        # --------------------------------------------------

        decision_result = results.get("decision")

        if (
            decision_result
            and decision_result.success
        ):

            self.decision_output_router.persist(
                db=event.db,
                user_id=event.user_id,
                result=decision_result.data,
            )

        # --------------------------------------------------
        # 5. Persist Reflection output
        # --------------------------------------------------

        reflection_result = results.get(
            "reflection"
        )

        if (
            reflection_result
            and reflection_result.success
        ):

            self.reflection_persistence.save(
                db=event.db,
                user_id=event.user_id,
                content=reflection_result.data,
            )

        return results