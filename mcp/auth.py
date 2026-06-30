class MCPAuthenticator:
    """
    Simple token-based authentication for the MCP layer.
    """
    def __init__(self, required_token: str = None):
        self._required_token = required_token

    def verify(self, headers: dict) -> bool:
        if not self._required_token:
            return True
            
        token = headers.get("Authorization", "").replace("Bearer ", "")
        return token == self._required_token
