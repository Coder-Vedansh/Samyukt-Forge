# Developer Documentation

Welcome to the Forge CLI core contributor guide!

## Setting up the Environment

1. Clone the repository.
2. Install dependencies via Hatch or pip:
```bash
pip install -e .[dev]
```

## Code Quality Standards

We strictly enforce:
- **Ruff** for linting and formatting.
- **Mypy** for static type checking.
- **Pytest** for testing (targeting 90% coverage).
- **Bandit/CodeQL** for security scans.

Before submitting a Pull Request, run the pre-commit hooks:
```bash
pre-commit run --all-files
```

## Architecture Principles
Ensure you read the Architecture Docs before modifying the `kernel/` or `runtime/` directories. We strictly adhere to SOLID principles and Dependency Injection.
