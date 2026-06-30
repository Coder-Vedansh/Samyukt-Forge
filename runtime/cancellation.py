import threading

class CancellationToken:
    """
    Enables graceful cooperative cancellation of running tasks.
    """
    def __init__(self):
        self._is_cancelled = False
        self._lock = threading.Lock()

    def cancel(self) -> None:
        with self._lock:
            self._is_cancelled = True

    @property
    def is_cancelled(self) -> bool:
        with self._lock:
            return self._is_cancelled

    def throw_if_cancelled(self) -> None:
        if self.is_cancelled:
            raise InterruptedError("Task execution was cancelled.")
