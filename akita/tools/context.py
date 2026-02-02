import os
from pathlib import Path
from typing import List, Dict, Optional
from pydantic import BaseModel

class FileContext(BaseModel):
    path: str
    content: str
    extension: str

class ContextSnapshot(BaseModel):
    files: List[FileContext]
    project_structure: List[str]

class ContextBuilder:
    def __init__(
        self, 
        base_path: str, 
        extensions: Optional[List[str]] = None,
        exclude_dirs: Optional[List[str]] = None,
        max_file_size_kb: int = 50,
        max_files: int = 50
    ):
        self.base_path = Path(base_path)
        self.extensions = extensions or [".py", ".js", ".ts", ".cpp", ".h", ".toml", ".md", ".json"]
        self.exclude_dirs = exclude_dirs or [".git", ".venv", "node_modules", "__pycache__", "dist", "build"]
        self.max_file_size_kb = max_file_size_kb
        self.max_files = max_files

    def build(self) -> ContextSnapshot:
        """Scan the path and build a context snapshot."""
        files_context = []
        project_structure = []
        
        if self.base_path.is_file():
            if self._should_include_file(self.base_path):
                files_context.append(self._read_file(self.base_path))
                project_structure.append(str(self.base_path.name))
        else:
            for root, dirs, files in os.walk(self.base_path):
                # Filter out excluded directories
                dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
                
                rel_root = os.path.relpath(root, self.base_path)
                if rel_root == ".":
                    rel_root = ""

                for file in files:
                    file_path = Path(root) / file
                    if self._should_include_file(file_path):
                        if len(files_context) < self.max_files:
                            context = self._read_file(file_path)
                            if context:
                                files_context.append(context)
                                project_structure.append(os.path.join(rel_root, file))
        
        return ContextSnapshot(files=files_context, project_structure=project_structure)

    def _should_include_file(self, path: Path) -> bool:
        if path.name == ".env" or path.suffix == ".env":
            return False
            
        if path.suffix not in self.extensions:
            return False
        
        if not path.exists():
            return False
            
        # Check size
        if path.stat().st_size > self.max_file_size_kb * 1024:
            return False
            
        return True

    def _read_file(self, path: Path) -> Optional[FileContext]:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                return FileContext(
                    path=str(path.relative_to(self.base_path) if self.base_path.is_dir() else path.name),
                    content=content,
                    extension=path.suffix
                )
        except Exception:
            return None
