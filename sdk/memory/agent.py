from sdk.memory.core import IMemoryStore


class IAgentMemory(IMemoryStore):
    """
    Scope: State isolated strictly to a specific Agent instance.
    Stores agent-specific contexts, behaviors, local variables, and learned persona details.
    """

    pass
