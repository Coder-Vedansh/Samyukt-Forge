import asyncio
from typing import Any, Awaitable, Callable


class WorkerPool:
    """
    Manages a pool of async workers to execute tasks concurrently.
    """

    def __init__(self, max_workers: int = 5):
        self.max_workers = max_workers
        self._semaphore = asyncio.Semaphore(max_workers)

    async def run(self, func: Callable[..., Awaitable[Any]], *args, **kwargs) -> Any:
        async with self._semaphore:
            return await func(*args, **kwargs)
