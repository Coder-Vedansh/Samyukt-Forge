from pathlib import Path
from typing import Optional

from workspace.db import WorkspaceDatabase


class WorkspaceManager:
    """
    Acts as the central authority for all filesystem operations in a Forge project.
    Creates and manages the `.forge/` directory structure.
    """

    DIRECTORIES = ["project", "state", "cache", "memory", "config", "plugins"]

    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir).resolve()
        self.forge_dir = self.root_dir / ".forge"
        self._db: Optional[WorkspaceDatabase] = None

    def init_workspace(self) -> None:
        """Initializes the .forge directory structure and database."""
        self.forge_dir.mkdir(parents=True, exist_ok=True)

        for dir_name in self.DIRECTORIES:
            (self.forge_dir / dir_name).mkdir(exist_ok=True)

        # Ensure database is initialized
        self.get_db()

    def get_path(self, internal_dir: str) -> Path:
        """Retrieves an absolute path to a specific internal workspace directory."""
        if internal_dir not in self.DIRECTORIES:
            raise ValueError(f"Unknown internal directory: {internal_dir}")
        path = self.forge_dir / internal_dir
        path.mkdir(parents=True, exist_ok=True)
        return path

    def get_db(self) -> WorkspaceDatabase:
        """Lazy loads the workspace SQLite database."""
        if not self._db:
            db_path = self.forge_dir / "workspace.db"
            self._db = WorkspaceDatabase(db_path)
        return self._db
