from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class NodeContext(BaseModel):
    """Context passed to a node during execution, containing the shared workflow state."""

    state: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Node(ABC):
    """Base class for any unit of work in a Forge Workflow."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    async def execute(self, context: NodeContext, **kwargs: Any) -> Any:
        """Executes the node's logic."""
        pass


class Edge(BaseModel):
    """Represents a directional transition between two Nodes."""

    source_node: str
    target_node: str
    condition: Optional[str] = None


class Graph(BaseModel):
    """A Directed Acyclic Graph (DAG) representing the state transitions of a workflow."""

    nodes: Dict[str, Any] = Field(default_factory=dict)  # Node instances
    edges: List[Edge] = Field(default_factory=list)


class Workflow(BaseModel):
    """The top-level orchestration container."""

    name: str
    description: Optional[str] = None
    graph: Graph
    entry_point: str
