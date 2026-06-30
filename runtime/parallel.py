import asyncio
from typing import Any, Awaitable, Callable, List

from runtime.worker_pool import WorkerPool


class ParallelExecutor:
    """
    Executes multiple tasks in parallel using a worker pool.
    """

    def __init__(self, pool: WorkerPool):
        self.pool = pool

    async def execute_all(self, tasks: List[Callable[[], Awaitable[Any]]]) -> List[Any]:
        coroutines = [self.pool.run(task) for task in tasks]
        return await asyncio.gather(*coroutines, return_exceptions=True)
