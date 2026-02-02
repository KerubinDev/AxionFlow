import litellm
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from akita.core.config import get_config_value

class Message(BaseModel):
    role: str
    content: str

class ModelResponse(BaseModel):
    content: str
    raw: Any

class AIModel:
    def __init__(self, model_name: str, api_key: Optional[str] = None, base_url: Optional[str] = None):
        self.model_name = model_name
        self.api_key = api_key
        self.base_url = base_url

    def chat(self, messages: List[Dict[str, str]], **kwargs) -> ModelResponse:
        """
        Send a chat completion request.
        """
        response = litellm.completion(
            model=self.model_name,
            messages=messages,
            api_key=self.api_key,
            base_url=self.base_url,
            **kwargs
        )
        content = response.choices[0].message.content
        return ModelResponse(content=content, raw=response)

def get_model(model_name: Optional[str] = None) -> AIModel:
    """
    Get an AIModel instance based on config or provided name.
    """
    if model_name is None:
        model_name = get_config_value("model", "name", "gpt-4o-mini")
    
    provider = get_config_value("model", "provider", "openai")
    
    # LiteLLM usually wants "provider/model_name" for some providers 
    # but for OpenAI it handles "gpt-3.5-turbo" directly.
    # If it's a custom provider, we might need to prepend it.
    full_model_name = f"{provider}/{model_name}" if provider != "openai" else model_name
    
    return AIModel(model_name=full_model_name)
