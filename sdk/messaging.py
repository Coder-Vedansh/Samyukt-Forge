from typing import Any, Dict

from pydantic import BaseModel


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
