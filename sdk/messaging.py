from pydantic import BaseModel
from typing import Any, Dict

class SDKEvent(BaseModel):
    """
    Public schema for Events that plugins can emit or subscribe to.
    """
    name: str
    payload: Dict[str, Any]

class SDKCommand(BaseModel):
    """
    Public schema for Commands that plugins can dispatch or handle.
    """
    name: str
    payload: Dict[str, Any]
