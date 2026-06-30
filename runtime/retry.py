import asyncio
import time
from typing import Any, Awaitable, Callable


class RetryPolicy:
    """
    Handles exponential backoff and retry logic for tasks that fail.
    """

    def __init__(self, max_retries: int = 3, base_delay: float = 1.0, multiplier: float = 2.0):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.multiplier = multiplier

    async def execute_async(self, func: Callable[..., Awaitable[Any]], *args, **kwargs) -> Any:
        attempt = 0
        delay = self.base_delay

        while attempt <= self.max_retries:
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                attempt += 1
                if attempt > self.max_retries:
                    raise e
                await asyncio.sleep(delay)
                delay *= self.multiplier

    def execute_sync(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        attempt = 0
        delay = self.base_delay

        while attempt <= self.max_retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempt += 1
                if attempt > self.max_retries:
                    raise e
                time.sleep(delay)
                delay *= self.multiplier
