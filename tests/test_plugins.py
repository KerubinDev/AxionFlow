import pytest
from akita.core.plugins import PluginManager, AkitaPlugin
from typing import List, Dict, Any

class MockPlugin(AkitaPlugin):
    @property
    def name(self) -> str:
        return "mock"
    @property
    def description(self) -> str:
        return "Mock plugin for tests"
    def get_tools(self) -> List[Dict[str, Any]]:
        return [{"name": "mock_tool", "description": "A mock tool", "func": lambda: "ok"}]

def test_plugin_discovery_internal():
    pm = PluginManager()
    pm.discover_all()
    # At least our official 'files' plugin should be found if it's in the path
    assert "files" in pm.plugins

def test_plugin_manager_get_tools():
    pm = PluginManager()
    # Manually register a mock plugin
    plugin = MockPlugin()
    pm.plugins["mock"] = plugin
    
    tools = pm.get_all_tools()
    assert len(tools) >= 1
    assert any(t["name"] == "mock_tool" for t in tools)

def test_reasoning_engine_uses_plugins(monkeypatch):
    from akita.reasoning.engine import ReasoningEngine
    from akita.models.base import AIModel
    
    class FakeModel(AIModel):
        def chat(self, messages): return type('obj', (object,), {'content': '{}'})()
    
    engine = ReasoningEngine(FakeModel(model_name="test-model"))
    # Should have loaded plugins during init
    assert len(engine.plugin_manager.plugins) > 0
    assert "files" in engine.plugin_manager.plugins
