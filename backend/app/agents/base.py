from abc import ABC, abstractmethod

from .context import AgentContext
from .result import AgentResult


class BaseAgent(ABC):
    """
    Base contract for all ECHO V2 agents.
    """

    name: str = "base"

    @abstractmethod
    def run(self, context: AgentContext) -> AgentResult:
        """
        Execute the agent using the shared context.
        """
        raise NotImplementedError