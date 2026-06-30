from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class TaskState(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class TaskContext(BaseModel):
    task_id: str
    state: TaskState = TaskState.PENDING
    result: Optional[Any] = None
    error: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def update_state(self, new_state: TaskState, result: Any = None, error: str = None) -> None:
        self.state = new_state
        if result is not None:
            self.result = result
        if error is not None:
            self.error = error
