# Contributing to Forge CLI

Thank you for your interest in contributing to Forge CLI! We welcome contributions from everyone.

## Development Setup

1. **Fork and Clone**: Fork the repository and clone it locally.
2. **Install Dependencies**: We use `uv` or `poetry`. Run `pip install -e ".[dev]"`.
3. **Pre-commit Hooks**: Run `pre-commit install` to ensure all commits pass linting.

## Branching Strategy

We follow GitHub Flow:
- Main branch (`main`) is always deployable.
- Create feature branches from `main` (e.g., `feat/add-new-provider`).
- Create bugfix branches from `main` (e.g., `fix/memory-leak`).

## Code Standards

- **Linting**: We strictly enforce `Ruff` for formatting and linting.
- **Type Checking**: We strictly enforce `Mypy`. Your code must pass `mypy .`
- **Testing**: All new features must include `pytest` unit tests. Code coverage must not drop.

## Pull Request Process

1. Ensure all tests pass (`pytest`).
2. Update documentation if necessary.
3. Submit a PR using the provided template.
4. A maintainer will review your code. You must address any feedback before merging.
