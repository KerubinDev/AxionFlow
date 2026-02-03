from akita.core.plugins import AkitaPlugin
from akita.tools.base import FileSystemTools
from typing import List, Dict, Any

class FilesPlugin(AkitaPlugin):
    @property
    def name(self) -> str:
        return "files"

    @property
    def description(self) -> str:
        return "Standard filesystem operations (read, write, list)."

    def get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "read_file",
                "description": "Read content from a file.",
                "parameters": {"path": "string"},
                "func": FileSystemTools.read_file
            },
            {
                "name": "write_file",
                "description": "Write content to a file.",
                "parameters": {"path": "string", "content": "string"},
                "func": FileSystemTools.write_file
            },
            {
                "name": "list_dir",
                "description": "List files in a directory.",
                "parameters": {"path": "string"},
                "func": FileSystemTools.list_dir
            }
        ]
