from abc import abstractmethod
from typing import Any, Dict, List

from pydantic import BaseModel

from sdk.engine.chat import ChatMessage
from sdk.engine.provider import IProvider


class ToolDefinition(BaseModel):
    name: str
    description: str
    parameters_schema: Dict[str, Any]


class ToolCall(BaseModel):
    id: str
    name: str
    arguments: str  # JSON string of arguments


class ToolCallResponse(BaseModel):
    message: ChatMessage
    tool_calls: List[ToolCall]
    usage: Dict[str, int]


class IToolCalling(IProvider):
    """Interface for models capable of constrained JSON and Tool/Function calling."""

    @abstractmethod
    async def chat_with_tools(
        self, model: str, messages: List[ChatMessage], tools: List[ToolDefinition], **kwargs: Any
    ) -> ToolCallResponse:
        """Send a conversation and a list of available tools, returning potential tool invocations."""
        pass
