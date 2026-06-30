# SDK Reference

The `forge_cli.sdk` package exposes all the tools necessary for developers to build extensions, agents, and orchestrators.

## Key Modules

### `sdk.agent`
Contains the `Agent` base class for defining AI behaviors.

### `sdk.tool`
Decorators and classes for exposing Python functions to LLMs.

### `sdk.llm`
Standardized interfaces (`ILLMProvider`) ensuring Forge is model-agnostic. Supports OpenAI, Anthropic, Gemini, etc.

### `sdk.memory`
Short-term (`MemoryWindow`) and long-term (`VectorStore`) memory abstractions.
