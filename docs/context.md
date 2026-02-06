# Intelligent Context and LiteRAG

Axion understands your code deeply.

## AST Analysis
Using Tree-sitter, Axion parses your Python files to identify types, classes, functions, and docstrings. This allows it to:
- Optimize token usage by selecting only pertinent code blocks.
- Provide higher accuracy for refactoring tasks.

## LiteRAG (Semantic Search)
For large repositories, Axion uses a built-in LiteRAG indexer.
- **index command**: `axion index .` creates a local searchable index.
- **Search**: When solving tasks, Axion finds semantic similarities to find the needle in the haystack.
- **Local**: 100% privacy. No vector data ever leaves your machine.
