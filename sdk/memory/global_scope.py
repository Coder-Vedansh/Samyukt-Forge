from sdk.memory.core import IMemoryStore


class IGlobalMemory(IMemoryStore):
    """
    Scope: User-level state shared across *all* Forge projects.
    E.g. User preferences, cross-project API keys, global agent configurations.
    """

    pass
