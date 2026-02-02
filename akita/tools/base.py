import subprocess
import os
from typing import List, Optional
from pydantic import BaseModel

class ToolResult(BaseModel):
    success: bool
    output: str
    error: Optional[str] = None

class FileSystemTools:
    @staticmethod
    def read_file(path: str) -> str:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def list_files(path: str) -> List[str]:
        return os.listdir(path)

class ShellTools:
    @staticmethod
    def execute(command: str, cwd: Optional[str] = None) -> ToolResult:
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                cwd=cwd,
                check=False
            )
            return ToolResult(
                success=result.returncode == 0,
                output=result.stdout,
                error=result.stderr if result.returncode != 0 else None
            )
        except Exception as e:
            return ToolResult(success=False, output="", error=str(e))
