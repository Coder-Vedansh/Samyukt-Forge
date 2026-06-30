# Forge CLI Architecture

Forge CLI is designed as a strict **Microkernel**, treating every AI capability (LLMs, Vector DBs, Agents, Orchestrators) as a decoupled plugin. It is heavily inspired by the architectures of Linux, VS Code, and Kubernetes.

## Core Layers

1. **Kernel (`kernel/`)**
   - The absolute core. It knows nothing about AI.
   - Manages the **Event Bus** (async Pub/Sub) and **Command Bus** (sync 1:1 routing).
   - Manages the **Plugin Loader**, hot-loading extensions via `importlib`.
   - Enforces the **Security Sandbox**, strictly managing permissions before routing commands.

2. **Extension SDK (`sdk/`)**
   - The developer contract. Defines abstract base classes like `IPlugin`, `ITool`, `IModelProvider`, and `IOrchestrator`.
   - External plugins strictly depend on this layer, never the Kernel.

3. **Runtime (`runtime/`)**
   - The execution engine. Manages DAG task scheduling, concurrent `WorkerPool` execution via `asyncio`, checkpoints, and cancellations.

4. **Package Manager (`package_manager/`)**
   - The "npm for AI". Handles discovering, downloading, and resolving dependencies (via SemVer Topological Sort) for plugins.

5. **MCP Layer (`mcp/`)**
   - Exposes Forge to the outside world using the standard Model Context Protocol via JSON-RPC over `stdio`.

6. **CLI (`cli/`)**
   - A `Typer`-based presentation layer routing user intents to the Kernel buses.
