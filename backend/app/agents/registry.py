from typing import Dict

from .base import BaseAgent


class AgentRegistry:
    """
    Central registry for ECHO V2 agents.

    The registry stores agent instances by name.
    It does not execute agents or decide workflow order.
    """

    def __init__(self):
        self._agents: Dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """
        Register an agent.
        """

        if agent.name in self._agents:
            raise ValueError(
                f"Agent '{agent.name}' is already registered."
            )

        self._agents[agent.name] = agent

    def get(self, name: str) -> BaseAgent:
        """
        Retrieve an agent by name.
        """

        if name not in self._agents:
            raise KeyError(
                f"Agent '{name}' is not registered."
            )

        return self._agents[name]

    def has(self, name: str) -> bool:
        """
        Check whether an agent is registered.
        """

        return name in self._agents

    def list_agents(self) -> list[str]:
        """
        Return registered agent names.
        """

        return list(self._agents.keys())