from typing import List

from pydantic import BaseModel


class PermissionScope(BaseModel):
    name: str
    description: str
    is_required: bool = True


class ISecurityContext(BaseModel):
    """
    Defines the permission manifest a plugin requests from the user.
    """

    requested_scopes: List[PermissionScope]
