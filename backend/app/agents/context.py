from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentContext:

    user: Optional[Any] = None

    user_id: Optional[Any] = None

    db: Optional[Any] = None

    current_memory: Optional[Any] = None

    current_state: Optional[Any] = None

    recent_memories: List[Any] = field(
        default_factory=list
    )

    memory_analysis: Optional[Any] = None

    twin_update: Optional[Any] = None

    goals: List[Any] = field(
        default_factory=list
    )

    planner_tasks: List[Any] = field(
        default_factory=list
    )

    insights: List[Any] = field(
        default_factory=list
    )

    snapshots: List[Any] = field(
        default_factory=list
    )

    trends: Optional[Any] = None

    simulation: Optional[Any] = None

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    agent_results: Dict[str, Any] = field(
        default_factory=dict
    )

    def store_result(
        self,
        agent_name: str,
        result: Any,
    ) -> None:
        self.agent_results[agent_name] = result

    def get_result(
        self,
        agent_name: str,
    ) -> Optional[Any]:
        return self.agent_results.get(agent_name)

    def get_state(
        self,
        domain: str,
    ) -> Optional[Any]:
        """
        Return the current state value
        for a specific domain.
        """

        for state in self.current_state or []:
            if state.domain.lower() == domain.lower():
                return state.value

        return None

    def get_recent_memory(
        self,
    ) -> Optional[Any]:
        """
        Return the most recent memory
        from the loaded context.
        """

        if not self.recent_memories:
            return None

        return self.recent_memories[0]

    def has_active_goals(
        self,
    ) -> bool:
        """
        Return True when at least one
        goal is not completed.
        """

        return any(
            not goal.completed
            for goal in self.goals
        )