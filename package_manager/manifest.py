import json
from pathlib import Path
from typing import Dict, List, Optional

from pydantic import BaseModel


class PluginDependency(BaseModel):
    name: str
    version_specifier: str


class PluginManifest(BaseModel):
    name: str
    version: str
    description: str
    dependencies: Dict[str, str] = {}


class PackageManifest(BaseModel):
    """Defines the metadata structure for a .forgepkg file."""

    name: str
    version: str
    description: str
    author: str
    dependencies: Dict[str, str] = {}
    entrypoint: str
    permissions: List[str] = []
    compatibility: str = ">=0.1.0"
    signature: Optional[str] = None


class ManifestManager:
    """
    Manages the forge.json file which acts like package.json for the workspace.
    """

    def __init__(self, workspace_dir: str):
        self.manifest_path = Path(workspace_dir) / "forge.json"

    def load(self) -> PluginManifest:
        if not self.manifest_path.exists():
            return PluginManifest(
                name="forge-workspace", version="1.0.0", description="Local Forge Workspace"
            )
        with open(self.manifest_path, "r") as f:
            return PluginManifest(**json.load(f))

    def save(self, manifest: PluginManifest) -> None:
        with open(self.manifest_path, "w") as f:
            f.write(manifest.model_dump_json(indent=2))

    def add_dependency(self, name: str, version: str) -> None:
        manifest = self.load()
        manifest.dependencies[name] = version
        self.save(manifest)

    def remove_dependency(self, name: str) -> None:
        manifest = self.load()
        if name in manifest.dependencies:
            del manifest.dependencies[name]
            self.save(manifest)
