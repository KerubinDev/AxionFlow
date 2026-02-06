import abc
import importlib
import importlib.metadata
import inspect
import pkgutil
from pathlib import Path
from typing import List, Dict, Any, Type, Optional

class AxionPlugin(abc.ABC):
    """Base class for all Axion plugins."""
    
    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Unique name of the plugin."""
        pass

    @property
    @abc.abstractmethod
    def description(self) -> str:
        """Brief description of what the plugin does."""
        pass

    @abc.abstractmethod
    def get_tools(self) -> List[Dict[str, Any]]:
        """Return a list of tools (functions) provided by this plugin."""
        pass

class PluginManager:
    def __init__(self, internal_plugins_path: Optional[str] = None):
        self.plugins: Dict[str, AxionPlugin] = {}
        self.internal_path = internal_plugins_path or str(Path(__file__).parent.parent / "plugins")

    def discover_all(self):
        """Discover both internal and external plugins."""
        self._discover_internal()
        self._discover_external()

    def _discover_internal(self):
        """Load plugins from the axion/plugins directory."""
        path = Path(self.internal_path)
        if not path.exists():
            return

        for loader, module_name, is_pkg in pkgutil.iter_modules([str(path)]):
            full_module_name = f"axion.plugins.{module_name}"
            try:
                module = importlib.import_module(full_module_name)
                self._load_from_module(module)
            except Exception as e:
                print(f"Error loading internal plugin {module_name}: {e}")

    def _discover_external(self):
        """Load plugins registered via entry_points (axion.plugins)."""
        try:
            # Python 3.10+
            eps = importlib.metadata.entry_points(group='axion.plugins')
            for entry_point in eps:
                try:
                    plugin_class = entry_point.load()
                    if inspect.isclass(plugin_class) and issubclass(plugin_class, AxionPlugin):
                        instance = plugin_class()
                        self.plugins[instance.name] = instance
                except Exception as e:
                    print(f"Error loading external plugin {entry_point.name}: {e}")
        except Exception:
            pass

    def _load_from_module(self, module):
        """Extract AxionPlugin classes from a module and instantiate them."""
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, AxionPlugin) and obj is not AxionPlugin:
                instance = obj()
                self.plugins[instance.name] = instance

    def get_all_tools(self) -> List[Dict[str, Any]]:
        """Collect all tools from all loaded plugins."""
        all_tools = []
        for plugin in self.plugins.values():
            all_tools.extend(plugin.get_tools())
        return all_tools
