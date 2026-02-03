import pytest
from akita.core.ast_utils import ASTParser
from akita.tools.context import ContextBuilder
from pathlib import Path

def test_ast_parser_definitions(tmp_path):
    code = """
class MyClass:
    \"\"\"My Class Doc\"\"\"
    def method_one(self):
        return 1

def top_function():
    \"\"\"Function Doc\"\"\"
    pass
"""
    file_path = tmp_path / "sample.py"
    file_path.write_text(code)
    
    parser = ASTParser()
    defs = parser.get_definitions(str(file_path))
    found_names = [d["name"] for d in defs]
    assert len(defs) == 3, f"Expected 3 definitions (MyClass, method_one, top_function), but found {len(defs)}: {found_names}"
    
    # Check class
    my_class = next(d for d in defs if d["name"] == "MyClass")
    assert my_class["type"] == "class"
    assert my_class["docstring"] == "My Class Doc"
    
    # Check method
    method = next(d for d in defs if d["name"] == "method_one")
    assert method["type"] == "function"
    
    # Check top function
    func = next(d for d in defs if d["name"] == "top_function")
    assert func["type"] == "function"
    assert func["docstring"] == "Function Doc"

def test_context_builder_semantic_summary(tmp_path):
    code = "def hello(): pass"
    file_path = tmp_path / "hello.py"
    file_path.write_text(code)
    
    builder = ContextBuilder(str(tmp_path), use_semantical_context=True)
    snapshot = builder.build()
    
    # Find hello.py context
    hello_ctx = next(f for f in snapshot.files if f.path == "hello.py")
    assert "FUNCTION hello" in hello_ctx.summary
