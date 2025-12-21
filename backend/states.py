from enum import Enum
from typing import Dict, Set

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

ALLOWED: Dict[TaskStatus, Set[TaskStatus]] = {
    TaskStatus.IN_PROGRESS: {TaskStatus.BLOCKED, TaskStatus.COMPLETED, TaskStatus.FAILED},
    TaskStatus.PENDING: {TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED},
    TaskStatus.BLOCKED: {TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED},
    TaskStatus.COMPLETED: set(),
    TaskStatus.FAILED: set(),
    TaskStatus.CANCELLED: set(),
}

def can_transition(src: TaskStatus, dst: TaskStatus) -> bool:
    return dst in ALLOWED.get(src, set())

def transition(current: TaskStatus, dst: TaskStatus) -> TaskStatus:
    if can_transition(current, dst):
        return dst
    raise ValueError(f"invalid transition {current} -> {dst}")