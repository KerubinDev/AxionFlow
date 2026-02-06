import json
from unittest.mock import MagicMock
from axion.reasoning.engine import ReasoningEngine
from axion.models.base import AIModel, ModelResponse
from axion.core.config import save_config

def test_mock_review():
    # Mock model
    mock_model = MagicMock(spec=AIModel)
    mock_response = ModelResponse(
        content=json.dumps({
            "summary": "The code is well structured but needs minor style adjustments.",
            "issues": [
                {"file": "axion/cli/main.py", "type": "style", "description": "Long lines", "severity": "low"}
            ],
            "strengths": ["Clear naming", "Modular"],
            "suggestions": ["Add type hints", "Improve docstrings"],
            "risk_level": "low"
        }),
        raw={}
    )
    mock_model.chat.return_value = mock_response
    
    engine = ReasoningEngine(mock_model)
    # We'll review the current directory
    result = engine.run_review(".")
    
    assert result.risk_level == "low"
    assert len(result.issues) == 1
    assert result.issues[0].file == "axion/cli/main.py"
    print("✅ Mock review test passed!")

if __name__ == "__main__":
    test_mock_review()
