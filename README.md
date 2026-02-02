# AkitaLLM

**AkitaLLM** is an open-source, local-first AI system designed for professional programming. It orchestrates existing LLMs (Ollama, OpenAI, Anthropic, etc.) through a strict **Plan-Execute-Validate** pipeline to ensure code quality and reliability.

## What is AkitaLLM?

AkitaLLM is a command-line interface (CLI) that helps you manage codebases with AI. Unlike simple chat interfaces, AkitaLLM:
- **Analyzes** your project structure and file content before proposing changes.
- **Plans** technical steps using a structured reasoning engine.
- **Solves** problems by generating Unified Diffs that you can review.
- **Validates** changes using local testing frameworks like `pytest`.

## Key Features

- **Local-First**: Developed with privacy and security in mind.
- **Model Agnostic**: Use any model supported by LiteLLM (GPT-4o, Claude, Llama 3 via Ollama).
- **Structured Output**: Code reviews and plans are presented in professional terminal tables and Markdown.
- **Security by Default**: Diffs are only applied with your explicit confirmation.
- **Support for .env**: Manage your API keys safely.

## Installation

```bash
# Clone the repository
git clone https://github.com/Your-Name/AkitaLLM.git
cd AkitaLLM

# Install in editable mode
pip install -e .
```

## Usage

### 1. Initial Setup
The first time you run a command, AkitaLLM will guide you through choosing a model.
```bash
akita review .
```

### 2. Code Review
Analyze files or directories for bugs, style, and security risks.
```bash
akita review src/
```

### 3. Solution Planning
Generate a technical plan for a complex task.
```bash
akita plan "Refactor the authentication module to support JWT"
```

### 4. Problem Solving
Generate a diff to solve a specific issue.
```bash
akita solve "Add error handling to the ReasoningEngine class"
```

## Configuration

AkitaLLM stores its configuration in `~/.akita/config.toml`. You can manage it via:
```bash
# View and change model settings
akita config model

# Reset all settings
akita config model --reset
```

## Contributing

We welcome contributions! Please check [CONTRIBUTING.md](CONTRIBUTING.md) to understand our workflow and standards.

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

*“Understanding the internals is the first step to excellence.”*
