import time
from typing import Any, Dict


class ExecutionMetrics:
    """
    Collects telemetry data for task and workflow execution.
    """

    def __init__(self):
        self.start_time: float = 0.0
        self.end_time: float = 0.0
        self.cpu_usage_estimation: float = 0.0
        self.memory_usage_estimation: float = 0.0
        self.custom_metrics: Dict[str, Any] = {}

    def start(self) -> None:
        self.start_time = time.time()

    def stop(self) -> None:
        self.end_time = time.time()

    @property
    def duration_seconds(self) -> float:
        if self.start_time == 0:
            return 0.0
        if self.end_time == 0:
            return time.time() - self.start_time
        return self.end_time - self.start_time

    def record(self, key: str, value: Any) -> None:
        self.custom_metrics[key] = value
