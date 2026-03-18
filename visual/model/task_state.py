from dataclasses import dataclass, field
from typing import Optional

from visual.model.task_progress import TaskProgress


@dataclass
class TaskState:
    """Task state data model"""
    task_name: str = ""
    status: str = ""  # running/completed/stopped/error/call_user
    progress: TaskProgress = field(default_factory=TaskProgress)
    error_msg: Optional[str] = None
    is_running: bool = False
    session_id: Optional[str] = None  # New: server session ID
    device_id: Optional[str] = None   # New: device ID
    platform_tag: Optional[str] = None# New: platform identifier