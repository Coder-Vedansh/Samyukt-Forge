# Command Line Interface (CLI)

Forge uses `Typer` and `Rich` to provide a beautiful, modern terminal experience.

## Commands

### `forge init`
Initializes a new `.forge` workspace in the current directory.

### `forge run`
Executes a specified Agent or Workflow.
**Usage:** `forge run <agent_name> --input "Hello"`

### `forge install`
Uses the Forge Package Manager to download and install a plugin.
**Usage:** `forge install mcp-github-server`

### `forge doctor`
Runs a diagnostic check on your environment, ensuring plugins load correctly and dependencies are met.
