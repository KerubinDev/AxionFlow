# Axion Roadmap: The Path to v1.0.0 🚀

This document outlines the strategic steps required to transition Axion from Beta to a stable, production-ready v1.0.0.

## 🎯 Phase 1: Robust Execution (The Core)
- [x] **Complete DiffApplier**: Implement full Unified Diff application with rollback capabilities.
- [x] **Atomicity**: Ensure multi-file changes are applied as a single transaction (all or nothing).
- [x] **Pre-flight Validation**: Automatically run tests or linters on the proposed diff before application.

## 🧠 Phase 2: Intelligent Context (AST & Semantics)
- [x] **AST Integration**: Use `Tree-sitter` to parse code structure and allow granular item targeting (classes, methods).
- [x] **Dependency Grafting**: Automatically include relevant imported files in the LLM context.
- [x] **Context Budgeting**: Intelligent token management to avoid hitting context limits on large files.

## 🔌 Phase 3: Plugin Architecture (Extensibility)
- [x] **Plugin Engine**: Implement a plugin system using Python `entry_points`.
- [x] **Core Plugins**: Move standard tools (Linter, Git) to a plugin-based internal structure.
- [x] **Third-Party Support**: Create a SDK/Template for developers to build their own Axion plugins. (See [PLUGINS.md](file:///c:/Users/kelvi/OneDrive/Área de Trabalho/Axion/PLUGINS.md))

## 🔄 Phase 4: Interactive Feedback Loop
- [x] **Human Review**: Allow users to review/edit the generated diff before application.
- [x] **Reasoning Trace**: Show why the LLM made specific decisions or selected certain files.
- [x] **Stateful Chat**: Enable follow-up questions to refine a solution.

## 📈 Phase 5: Production & Enterprise Grade
- [ ] **Binary Releases**: Compile Axion as standalone binaries (Windows, Linux, macOS).
- [ ] **Local Search (RAG)**: Integrate local vector database (FAISS/ChromaDB) for high-performance context retrieval.
- [ ] **Comprehensive Documentation Site**: Professional technical documentation outside of GitHub.

---

*“Engineering is not about the first version, it’s about the tenth version’s stability.”*
