from typing import List, Dict, Any, Optional
from datetime import datetime
import time
from pydantic import BaseModel, Field
from rich.table import Table
from rich.console import Console


_current_trace = None

def get_current_trace():
    return _current_trace

def set_current_trace(trace):
    global _current_trace
    _current_trace = trace

class TraceStep(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.now)
    perf_time: float = Field(default_factory=time.perf_counter)
    action: str
    details: str
    status: str = "OK"  # OK, FAIL, SKIPPED
    duration: Optional[float] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ReasoningTrace(BaseModel):
    steps: List[TraceStep] = Field(default_factory=list)

    def add_step(self, action: str, details: str, status: str = "OK", metadata: Dict[str, Any] = None):
        step = TraceStep(action=action, details=details, status=status, metadata=metadata or {})
        
        # Calculate duration if there was a previous step
        if self.steps:
            prev_step = self.steps[-1]
            prev_step.duration = step.perf_time - prev_step.perf_time
            
        self.steps.append(step)

    def finish_last_step(self):
        """Sets duration for the final step."""
        if self.steps and self.steps[-1].duration is None:
            self.steps[-1].duration = time.perf_counter() - self.steps[-1].perf_time

    def get_report_table(self) -> Table:
        self.finish_last_step()
        table = Table(title="AxionFlow Execution Report", show_header=True, header_style="bold blue")
        table.add_column("Step", style="white")
        table.add_column("Status", justify="center")
        table.add_column("Details", style="dim")
        table.add_column("Time", justify="right")

        for step in self.steps:
            status_color = "green" if step.status == "OK" else "red" if step.status == "FAIL" else "yellow"
            status_icon = "[OK]" if step.status == "OK" else "[FAIL]" if step.status == "FAIL" else "[-]"
            
            duration_str = f"{step.duration:.2f}s" if step.duration is not None else "-"
            
            table.add_row(
                step.action,
                f"[{status_color}]{status_icon}[/]",
                step.details,
                duration_str
            )
        return table

    def __str__(self):
        return "\n".join([f"[{s.timestamp.strftime('%H:%M:%S')}] {s.action} ({s.status}): {s.details}" for s in self.steps])
