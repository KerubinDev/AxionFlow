# AkitaLLM

![PyPI](https://img.shields.io/pypi/v/akitallm)
![Python](https://img.shields.io/pypi/pyversions/akitallm)
![License](https://img.shields.io/github/license/KerubinDev/AkitaLLM)
[![Tests](https://img.shields.io/github/actions/workflow/status/KerubinDev/AkitaLLM/tests.yml)](https://github.com/KerubinDev/AkitaLLM/actions)
![Downloads](https://img.shields.io/pypi/dm/akitallm)


```

Analyze → Plan → Execute → Validate

````

**A deterministic, local-first AI orchestrator for software engineers.**

AkitaLLM is not a chat interface.
It is not autocomplete.
It is not “AI magic”.

It is an engineering tool.

---

## What AkitaLLM is (and what it is not)

AkitaLLM treats Large Language Models as **non-deterministic execution engines** that must operate inside a **strict, auditable pipeline**.

Instead of asking an AI *“please fix my code”*, you force it to:

1. **Analyze** the real project structure
2. **Plan** concrete technical steps
3. **Execute** changes as reviewable diffs
4. **Validate** results with real tooling

No hidden prompts.  
No blind edits.  
No guessing.

---

## Why this project exists

Most AI coding tools optimize for **speed of output**.

Software engineering optimizes for:
- correctness
- predictability
- debuggability
- long-term maintainability

That mismatch causes real problems:

- Code is generated without understanding the project
- Developers approve changes they don’t fully understand
- Bugs are pushed faster, not fewer

AkitaLLM exists to **slow AI down** and force it to behave like a junior engineer working under strict supervision.

---

## The core difference

| Aspect | Typical AI Tools | AkitaLLM |
|------|-----------------|----------|
| Interaction | Chat / Autocomplete | Structured pipeline |
| Control | Implicit | Explicit and reviewable |
| Output | Raw code | Unified diffs |
| Context | Prompt-limited | Project-aware |
| Validation | Manual | Automated |
| Philosophy | “Trust the model” | “Trust the process” |

---

## Design principles

**Local-first**  
Your code stays on your machine. AkitaLLM runs locally and only sends what is strictly necessary to the model.

**No magic**  
Every decision is logged. Every step is inspectable. Every change is explicit.

**Tool-driven**  
The AI uses tools (AST parsing, tests, linters). It does not replace them.

**Human-in-the-loop**  
Nothing is applied without your approval.

---

## What AkitaLLM can do today

- 🔍 **Structural code reviews**  
  Detect bugs, architectural risks, performance issues, and security problems.

- 🧭 **Technical planning**  
  Generate step-by-step implementation plans in Markdown.

- 🧩 **Diff-based solutions**  
  Propose changes as standard unified diffs — no direct file mutation.

- 🧪 **Local validation**  
  Run tests and tooling before applying changes.

- 🔌 **Extensible architecture**  
  Plugin system for custom tools and workflows.

- 🤖 **Model agnostic**  
  Works with OpenAI, Anthropic, Ollama, and any LiteLLM-compatible provider.

---

## Installation

```bash
pip install akitallm
````

Python 3.10+ required.

---

## Basic usage

### Initialize / Review a project

```bash
akita review .
```

### Generate a technical plan

```bash
akita plan "Refactor authentication to use JWT with refresh tokens"
```

### Solve a concrete problem

```bash
akita solve "Fix silent failures in the reasoning engine error handling"
```

All commands follow the same pipeline:

```
Analyze → Plan → Execute → Validate
```

---

## Extending AkitaLLM

AkitaLLM is designed to be extended by engineers.

* Custom tools
* Custom validators
* Custom reasoning steps

See the [Plugin Development Guide](PLUGINS.md).

---

## Contributing

AkitaLLM is not looking for volume.
It is looking for **engineering-quality contributions**.

If you care about:

* clean abstractions
* predictable systems
* readable diffs
* testable behavior

You’ll fit right in.

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

> “Understanding the internals is the first step to excellence.”
