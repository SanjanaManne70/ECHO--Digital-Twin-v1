from dataclasses import dataclass, field
from typing import List


@dataclass
class AgentStep:
    """
    Defines one step in an ECHO V2 workflow.
    """

    agent_name: str

    depends_on: List[str] = field(default_factory=list)

    run_if_dependencies_failed: bool = False