# Forge CLI Testing Strategy

This document outlines the comprehensive, production-grade testing strategy for Forge CLI to ensure the stability, security, and scalability of the Microkernel architecture.

## The Testing Pyramid
The Forge CLI testing strategy strictly follows the **Testing Pyramid**. 
- **Base (Unit Tests)**: The vast majority of our tests. They are blazing fast, highly isolated, and test individual methods or classes (e.g., testing the `CommandBus` routing). They run on every single commit.
- **Middle (Integration/Contract Tests)**: Tests how modules interact (e.g., testing the `PluginLoader` with a dummy plugin). Slower than unit tests, but provide higher confidence.
- **Top (E2E/CLI/Performance Tests)**: The smallest number of tests. They test the system from the user's perspective (e.g., running `forge init` in a temporary directory). These are the slowest and run primarily on Pull Requests or Nightly builds.

---

## 1. Unit Tests
- **Objective**: Validate the logic of isolated components.
- **Scope**: `kernel/`, `runtime/`, `sdk/`, `package_manager/`.
- **Tooling**: `pytest` with `unittest.mock` for isolating dependencies (e.g., mocking the `EventBus` when testing the `Logger`).
- **Standard**: 90%+ code coverage enforced via CI.

## 2. Integration Tests
- **Objective**: Validate that multiple kernel sub-systems interact correctly.
- **Scope**: e.g., Ensuring `LifecycleManager` correctly calls `on_boot()` on a loaded plugin, or `TaskScheduler` correctly pipes a task to `TaskExecutor`.
- **Tooling**: `pytest` and `pytest-asyncio`. Tests use actual `EventBus` and `CommandBus` instances without mocks.

## 3. Plugin Tests
- **Objective**: Ensure that 3rd-party plugins adhere to the SDK contract without crashing the host.
- **Scope**: Loading a suite of intentionally malicious or malformed plugins into the `PluginSandbox` to verify they are rejected.
- **Tooling**: A dedicated fixture directory containing dummy `IPlugin` implementations.

## 4. CLI Tests
- **Objective**: Validate the Typer CLI presentation layer.
- **Scope**: `cli/` module.
- **Tooling**: Typer's `CliRunner`. We will simulate users typing commands like `forge run "hello"` and assert the stdout output and exit codes.

## 5. Runtime Tests
- **Objective**: Validate the DAG, concurrency, and async execution engine.
- **Scope**: `runtime/`.
- **Tooling**: `pytest-asyncio`. Tests will heavily involve `asyncio.sleep` mocks to verify `WorkerPool` semaphore limits and `ParallelExecutor` scatter-gather logic.

## 6. Performance Tests
- **Objective**: Prevent latency regressions in the Kernel buses.
- **Scope**: Measuring how many messages per second the `EventBus` and `CommandBus` can process.
- **Tooling**: `pytest-benchmark`. We will assert that resolving a dependency graph of 100 plugins takes < 50ms.

## 7. Security Tests
- **Objective**: Validate the Capability-based Sandbox and MCP Authentication.
- **Scope**: `kernel/security/` and `mcp/auth.py`.
- **Tooling**: Unit tests verifying that plugins lacking the `fs:write` scope in their `PermissionManifest` throw a `PermissionDeniedError` when attempting a write command via the bus.

## 8. Regression Tests
- **Objective**: Ensure previously fixed bugs do not re-emerge.
- **Scope**: Every time a GitHub Issue is closed as a bug, a specific test labeled `@pytest.mark.regression(issue_id="123")` must be added to the test suite before the PR is merged.

## 9. Snapshot Tests
- **Objective**: Validate the exact stdout formatting of complex CLI outputs (like Rich tables).
- **Scope**: `cli/`.
- **Tooling**: `pytest-snapshot` or `syrupy`. If the layout of `forge packages list` changes unexpectedly, the test fails.

## 10. Contract Tests
- **Objective**: Validate the MCP (Model Context Protocol) API boundaries.
- **Scope**: `mcp/server.py` and `mcp/client.py`.
- **Tooling**: We will use Consumer-Driven Contract testing. We assert that our `MCPToolRegistry` outputs JSON-RPC schemas that perfectly match the official Model Context Protocol JSON Schema specifications.
