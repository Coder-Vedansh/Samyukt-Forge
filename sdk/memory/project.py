from sdk.memory.core import IMemoryStore


class IProjectMemory(IMemoryStore):
    """
    Scope: Persistent state bound to the broader project context.
    E.g. Codebase analysis, git history summarizations, project-wide goals.
    """

    pass
