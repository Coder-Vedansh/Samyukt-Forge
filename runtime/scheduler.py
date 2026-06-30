from typing import List, Dict, Any
from runtime.state import TaskContext, TaskState

class TaskScheduler:
    """
    Schedules tasks based on dependencies and puts them in an execution queue.
    """
    def __init__(self):
        self._tasks: Dict[str, TaskContext] = {}
        self._queue: List[str] = []

    def schedule(self, task_id: str, dependencies: List[str] = None) -> None:
        context = TaskContext(task_id=task_id, state=TaskState.PENDING)
        self._tasks[task_id] = context
        
        # For simplicity, just append to queue. 
        # A real DAG scheduler would verify all dependencies are SUCCESS before queuing.
        self._queue.append(task_id)

    def get_next_task(self) -> TaskContext:
        if self._queue:
            task_id = self._queue.pop(0)
            return self._tasks[task_id]
        return None
