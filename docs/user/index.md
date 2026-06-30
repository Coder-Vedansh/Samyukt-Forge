# User Documentation

This section is for end-users who want to install Forge CLI and run pre-built agents or plugins.

## Installation

```bash
pip install forge-cli
```

## Basic Concepts

- **Workspace**: Your `.forge/` directory containing configurations, memory, and local plugins.
- **Agent**: An autonomous entity running in the runtime.
- **Tool**: An MCP or native python function exposed to agents.

## Common Commands

- `forge init`: Initializes a workspace in the current directory.
- `forge install <package>`: Installs a Forge extension from the registry.
- `forge run <agent>`: Spawns an agent in the runtime.
