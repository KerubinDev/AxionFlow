# Strategic Initial Issues

These issues are designed to help new contributors get started with Axion.

## 1. Documentation: Add Docstrings and Type Hints
**Label**: `documentation`, `good first issue`
**Description**: 
Many core functions in `axion/core/config.py` and `axion/tools/context.py` are missing proper Python docstrings and type hints.
**Goal**: Update all functions to follow the PEP 257 docstring convention and ensure 100% type hint coverage.

## 2. Feature: Implement Linter Tool
**Label**: `enhancement`, `help wanted`
**Description**: 
Axion should be able to run `flake8` or `black --check` as part of its validation pipeline.
**Goal**: Create a new tool in `axion/tools/linter.py` that can run a chosen linter and return a structured report to the `ReasoningEngine`.

## 3. Bug: DiffApplier path resolution on Windows
**Label**: `bug`
**Description**: 
The `DiffApplier` might have issues resolving relative paths correctly when the diff header uses forward slashes but the OS is Windows.
**Goal**: Ensure `Path` objects are used consistently in `axion/tools/diff.py` to handle cross-platform path resolution.
