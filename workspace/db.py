import sqlite3
from pathlib import Path


class WorkspaceDatabase:
    """Manages the internal SQLite database (workspace.db) for the local Forge workspace."""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_schema()

    def get_connection(self) -> sqlite3.Connection:
        """Returns a connection to the SQLite database."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self):
        """Initializes the database schema if it doesn't exist."""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # Cache Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cache (
                    key TEXT PRIMARY KEY,
                    value BLOB,
                    expires_at TIMESTAMP
                )
            """)

            # Memory Index Table (for Vector Store metadata)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS memory_index (
                    id TEXT PRIMARY KEY,
                    agent_id TEXT,
                    document_path TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # State Checkpoints Table (for long-running Tasks)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS checkpoints (
                    task_id TEXT PRIMARY KEY,
                    state BLOB,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            conn.commit()
