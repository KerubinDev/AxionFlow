# Strategic Initial Issues

These issues are designed to help new contributors get started with AkitaLLM.

## 1. Documentation: Add Docstrings and Type Hints
**Label**: `documentation`, `good first issue`
**Description**: 
Many core functions in `akita/core/config.py` and `akita/tools/context.py` are missing proper Python docstrings and type hints.
**Goal**: Update all functions to follow the PEP 257 docstring convention and ensure 100% type hint coverage.

## 2. Feature: Implement Linter Tool
**Label**: `enhancement`, `help wanted`
**Description**: 
AkitaLLM should be able to run `flake8` or `black --check` as part of its validation pipeline.
**Goal**: Create a new tool in `akita/tools/linter.py` that can run a chosen linter and return a structured report to the `ReasoningEngine`.

## 3. Bug: DiffApplier path resolution on Windows
**Label**: `bug`
**Description**: 
The `DiffApplier` might have issues resolving relative paths correctly when the diff header uses forward slashes but the OS is Windows.
**Goal**: Ensure `Path` objects are used consistently in `akita/tools/diff.py` to handle cross-platform path resolution.
