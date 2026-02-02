from typing import List, Literal
from pydantic import BaseModel, Field

class ReviewIssue(BaseModel):
    file: str = Field(description="Path to the file containing the issue")
    type: str = Field(description="Category of the issue: bug, style, performance, security, architecture")
    description: str = Field(description="Objective description of the problem")
    severity: Literal["low", "medium", "high"] = Field(description="Severity levels")

class ReviewResult(BaseModel):
    summary: str = Field(description="General summary of the code quality")
    issues: List[ReviewIssue] = Field(description="List of identified issues")
    strengths: List[str] = Field(description="Notable positive patterns in the codebase")
    suggestions: List[str] = Field(description="Global suggestions for improvement")
    risk_level: Literal["low", "medium", "high"] = Field(description="Overall risk level")
