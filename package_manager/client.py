from typing import Any, Dict, List


class RegistryClient:
    """
    Communicates with the Forge Plugin Marketplace (or PyPI) to search and fetch metadata.
    """

    def __init__(self, registry_url: str = "https://registry.forge-cli.com"):
        self.registry_url = registry_url

    async def search(self, query: str) -> List[Dict[str, Any]]:
        """Searches the remote registry for plugins matching the query."""
        # Simulated response for blueprint
        return [
            {"name": "forge-openai", "version": "1.0.0", "description": "OpenAI Provider Plugin"},
            {
                "name": "forge-langgraph",
                "version": "0.9.1",
                "description": "LangGraph Orchestrator",
            },
        ]

    async def get_package_info(self, package_name: str) -> Dict[str, Any]:
        """Fetches metadata, latest version, and dependencies for a remote package."""
        # Simulated response
        if package_name == "forge-openai":
            return {"name": "forge-openai", "latest": "1.0.0", "dependencies": {}}
        raise ValueError(f"Package {package_name} not found in registry.")

    async def publish(self, package_path: str, token: str) -> bool:
        """Publishes a local built package to the remote registry."""
        # Simulated upload
        return True
