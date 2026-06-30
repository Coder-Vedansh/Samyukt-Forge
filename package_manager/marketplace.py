from typing import Any, Dict, List, Optional


class MarketplaceClient:
    """
    Client for interacting with the Forge Plugin Marketplace API.
    Supports both public and private registries.
    """

    def __init__(self, registry_url: str = "https://api.forge-cli.com"):
        self.registry_url = registry_url

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Mock search for plugins."""
        # In a real implementation, this would be an HTTP GET to /search?q=query
        mock_db = [
            {
                "name": "mcp-github",
                "version": "1.0.0",
                "description": "GitHub MCP Server",
                "author": "Forge Team",
                "rating": 4.9,
            },
            {
                "name": "mcp-postgres",
                "version": "1.2.0",
                "description": "PostgreSQL MCP Server",
                "author": "Forge Team",
                "rating": 4.5,
            },
        ]
        return [
            pkg
            for pkg in mock_db
            if query.lower() in pkg["name"].lower() or query.lower() in pkg["description"].lower()
        ]

    def get_metadata(self, package_name: str) -> Optional[Dict[str, Any]]:
        """Mock retrieving package metadata."""
        if package_name == "mcp-github":
            return {
                "name": "mcp-github",
                "version": "1.0.0",
                "dependencies": {},
                "permissions": ["network:github.com"],
                "download_url": f"{self.registry_url}/packages/mcp-github-1.0.0.forgepkg",
            }
        return None

    def publish(self, package_path: str, auth_token: str) -> bool:
        """Mock publishing a local .forgepkg to the registry."""
        if not auth_token:
            raise ValueError("Authentication required to publish.")
        # In a real implementation, this would be a multipart/form-data POST
        return True

    def get_ratings(self, package_name: str) -> Dict[str, Any]:
        """Mock retrieving package ratings and reviews."""
        return {
            "average_rating": 4.9,
            "total_reviews": 128,
            "reviews": [{"user": "alice", "rating": 5, "comment": "Works great!"}],
        }
