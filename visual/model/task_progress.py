from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class TaskProgress:
    """Task progress data model"""
    step_idx: int = 0
    action: str = ""
    reasoning: str = ""
    action_meta: Dict[str, Any] = field(default_factory=dict)