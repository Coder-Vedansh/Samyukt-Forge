from sdk.memory.core import IMemoryStore


class ITemporaryMemory(IMemoryStore):
    """
    Scope: Ephemeral scratchpad.
    Bound to the lifecycle of a specific task or run. Flushed immediately upon completion.
    """

    pass
