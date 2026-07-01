from sdk.memory.core import IMemoryStore


class IWorkspaceMemory(IMemoryStore):
    """
    Scope: State bound to the current `.forge` directory.
    Used for caching, local databases, and workspace-specific configuration.
    """

    pass
