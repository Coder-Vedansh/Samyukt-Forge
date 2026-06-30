from typing import Dict
from runtime.state import TaskState

class ProgressTracker:
    """
    Calculates progress across a workflow DAG or job set.
    """
    def __init__(self, total_tasks: int):
        self.total_tasks = total_tasks
        self.task_states: Dict[str, TaskState] = {}

    def update_task(self, task_id: str, state: TaskState) -> float:
        self.task_states[task_id] = state
        return self.get_percentage()

    def get_percentage(self) -> float:
        if self.total_tasks == 0:
            return 100.0
            
        completed = sum(
            1 for state in self.task_states.values() 
            if state in (TaskState.SUCCESS, TaskState.FAILED, TaskState.CANCELLED)
        )
        return (completed / self.total_tasks) * 100.0
