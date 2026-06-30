# Architecture

Forge CLI is built as a Microkernel.

## The Kernel
The `kernel` package acts as the central router for all system events and commands. It contains:
- **EventBus**: Pub/Sub architecture for loosely coupled modules.
- **CommandBus**: CQRS-style RPC for direct module-to-module requests.
- **PluginOrchestrator**: Manages the lifecycle and sandboxing of all extensions.

## The Runtime
The `runtime` executes Agents. It consists of:
- **TaskScheduler**: A DAG-based async task graph.
- **WorkerPool**: Manages parallel execution limits.
- **Checkpointing**: State-saving to pause and resume workflows.

## Process Isolation
In upcoming versions, Forge CLI will transition from `importlib`-based plugins to Wasm or IPC-isolated plugins for guaranteed memory safety.
