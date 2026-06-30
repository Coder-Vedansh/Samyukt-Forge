from typing import Any, Awaitable, Callable

from runtime.cancellation import CancellationToken
from runtime.retry import RetryPolicy
from runtime.state import TaskContext, TaskState


class TaskExecutor:
    """
    Executes a single task, managing state transitions, cancellation, and retries.
    """

    def __init__(self, retry_policy: RetryPolicy):
        self.retry_policy = retry_policy

    async def execute(
        self, context: TaskContext, func: Callable[..., Awaitable[Any]], token: CancellationToken
    ) -> None:
        context.update_state(TaskState.RUNNING)
        try:
            token.throw_if_cancelled()
            result = await self.retry_policy.execute_async(func)
            context.update_state(TaskState.SUCCESS, result=result)
        except InterruptedError:
            context.update_state(TaskState.CANCELLED)
        except Exception as e:
            context.update_state(TaskState.FAILED, error=str(e))
