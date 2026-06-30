import json
from typing import Dict, Any
from pathlib import Path

class CheckpointManager:
    """
    Handles saving and resuming state so workflows can be paused and resumed.
    """
    def __init__(self, storage_dir: str):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def save_checkpoint(self, workflow_id: str, state: Dict[str, Any]) -> None:
        path = self.storage_dir / f"{workflow_id}.checkpoint.json"
        with open(path, "w") as f:
            json.dump(state, f, indent=2)

    def load_checkpoint(self, workflow_id: str) -> Dict[str, Any]:
        path = self.storage_dir / f"{workflow_id}.checkpoint.json"
        if not path.exists():
            return {}
        with open(path, "r") as f:
            return json.load(f)

    def clear_checkpoint(self, workflow_id: str) -> None:
        path = self.storage_dir / f"{workflow_id}.checkpoint.json"
        if path.exists():
            path.unlink()
