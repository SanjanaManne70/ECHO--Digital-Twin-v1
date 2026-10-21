from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentResult:
    """
    Standard result returned by an ECHO agent.
    """

    success: bool

    agent_name: str

    data: Optional[Any] = None

    message: Optional[str] = None

    errors: List[str] = field(default_factory=list)

    metadata: Dict[str, Any] = field(default_factory=dict)