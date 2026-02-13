from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ChatMessage(BaseModel):
    role: str
    content: Optional[str] = None
    name: Optional[str] = None
    tool_calls: Optional[Any] = None
    tool_call_id: Optional[str] = None

class ConversationSession(BaseModel):
    messages: List[ChatMessage] = Field(default_factory=list)

    def add_message(self, role: str, content: Optional[str] = None, **kwargs):
        self.messages.append(ChatMessage(role=role, content=content, **kwargs))

    def get_messages_dict(self) -> List[Dict[str, Any]]:
        # model_dump(exclude_none=True) is perfect for LiteLLM
        return [m.model_dump(exclude_none=True) for m in self.messages]
