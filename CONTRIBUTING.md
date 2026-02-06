# Contributing to Axion

Welcome! We are thrilled that you want to contribute to Axion. This project aims to be the most reliable local-first AI system for programmers.

## 🚀 How to Get Started

### 1. Fork and Clone
Fork the repository on GitHub and clone your fork locally:
```bash
git clone https://github.com/YOUR_USERNAME/Axion.git
cd Axion
```

### 2. Environment Setup
We recommend using a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
```

### 3. Running Tests
Ensure everything is working correctly:
```bash
pytest
```

## 🛠️ Contribution Flow

1. **Create a branch**: `git checkout -b feat/your-feature-name` or `fix/issue-description`.
2. **Implement changes**: Keep functions small, use type hints, and follow existing patterns.
3. **Write tests**: Every new feature or fix must have at least basic test coverage in `tests/`.
4. **Update Docs**: If you change the CLI or configuration, update `README.md`.
5. **Commit**: Use clear, descriptive commit messages.
6. **Pull Request**: Submit your PR with the provided template.

## 📏 Standards

### Code Quality
- **Type Hints**: Mandatory for all new functions.
- **Simplicity**: Favor obvious code over "clever" one-liners.
- **Security**: Never hardcode API keys. Use `.env` support.

### Git Hygiene
- Avoid large PRs. Split them into logical chunks if possible.
- Rebase your branch with `main` before submitting.

## 🎯 What we are looking for
- Better **Reasoning Engine** strategies.
- New **Tools** (e.g., Linter integration, AST parsers).
- Bug fixes and documentation improvements.

Thank you for helping Axion grow! 🚀
