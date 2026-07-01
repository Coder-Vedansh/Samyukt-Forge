from abc import abstractmethod
from typing import Any, Dict

from sdk.agents.cost import AgentCost
from sdk.agents.goals import AgentGoal
from sdk.agents.identity import AgentIdentity
from sdk.agents.lifecycle import IAgentLifecycle
from sdk.agents.memory import AgentMemoryBindings
from sdk.agents.metrics import AgentMetrics
from sdk.agents.permissions import AgentPermissions
from sdk.agents.policies import AgentPolicies
from sdk.agents.state import AgentState
from sdk.agents.tools import AgentToolRegistry


class IAgent(IAgentLifecycle):
    """
    The unified Agent interface.
    An agent is a strict composition of its Identity, Memory, Permissions, Tools, Goals, Policies, State, Metrics, and Cost.
    """

    @property
    @abstractmethod
    def identity(self) -> AgentIdentity:
        pass

    @property
    @abstractmethod
    def memory(self) -> AgentMemoryBindings:
        pass

    @property
    @abstractmethod
    def permissions(self) -> AgentPermissions:
        pass

    @property
    @abstractmethod
    def tools(self) -> AgentToolRegistry:
        pass

    @property
    @abstractmethod
    def goal(self) -> AgentGoal:
        pass

    @property
    @abstractmethod
    def policies(self) -> AgentPolicies:
        pass

    @property
    @abstractmethod
    def state(self) -> AgentState:
        pass

    @property
    @abstractmethod
    def metrics(self) -> AgentMetrics:
        pass

    @property
    @abstractmethod
    def cost(self) -> AgentCost:
        pass

    @abstractmethod
    async def invoke(self, inputs: Dict[str, Any]) -> str:
        """Triggers the agent to act on its goals based on the provided inputs."""
        pass
