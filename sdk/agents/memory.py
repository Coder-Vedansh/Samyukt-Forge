from typing import Optional

from sdk.memory.agent import IAgentMemory
from sdk.memory.conversation import IConversationMemory
from sdk.memory.workspace import IWorkspaceMemory


class AgentMemoryBindings:
    """
    Binds an agent to explicit memory scopes defined in Phase 17.
    """

    def __init__(
        self,
        agent_memory: IAgentMemory,
        conversation: IConversationMemory,
        workspace: Optional[IWorkspaceMemory] = None,
    ):
        self.internal = agent_memory
        self.conversation = conversation
        self.workspace = workspace
