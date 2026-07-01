from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class ToolSchema(BaseModel):
    """Base class for Tool Input/Output mathematical proofs."""

    @classmethod
    def json_schema(cls) -> Dict[str, Any]:
        """Returns the JSON schema representation required for LLM tool calling."""
        return cls.model_json_schema()


class InputSchema(ToolSchema):
    """
    Defines the exact shape of data a tool requires to execute.
    Any parameters strictly defined here will be coerced by the Orchestrator before passing to the tool.
    """

    pass


class OutputSchema(ToolSchema):
    """
    Defines the exact shape of data a tool returns upon successful execution.
    """

    error: Optional[str] = Field(
        default=None, description="Populated if the tool execution failed."
    )
