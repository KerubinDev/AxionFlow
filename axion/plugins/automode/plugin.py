
from axion.core.plugins import AxionPlugin
from axion.core.trace import get_current_trace
from axion.tools.diff import DiffApplier
from axion.tools.base import ShellTools
from axion.models.base import get_model
from typing import List, Dict, Any, Optional
import json
import traceback

class AutoModePlugin(AxionPlugin):
    @property
    def name(self) -> str:
        return "automode"

    @property
    def description(self) -> str:
        return "Autonomous development mode. Executes the full Plan-Code-Validate loop for a given task."

    def get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "execute_full_feature",
                "description": "Autonomously implement a feature or fix a bug. Handles planning, coding, and testing.",
                "parameters": {
                    "task": "string",
                    "max_iterations": "integer",
                    "human_check": "boolean"
                },
                "func": self.execute_full_feature
            }
        ]

    def execute_full_feature(self, task: str, max_iterations: int = 10, human_check: bool = False) -> str:
        """
        Executes the Plan-Code-Validate loop.
        """
        trace = get_current_trace()
        if trace:
            trace.add_step("AutoMode", f"Starting autonomous execution for: {task}", metadata={"max_iterations": max_iterations})

        # Lazy import to avoid circular dependency
        from axion.reasoning.engine import ReasoningEngine
        
        try:
            model = get_model()
            engine = ReasoningEngine(model)
            
            # 1. Plan (Optional but good for context)
            plan = engine.run_plan(task)
            if trace:
                trace.add_step("AutoMode", "Plan generated", details=plan[:100] + "...")

            # 2. Iterate
            iterations_used = 0
            history = [] # To keep track of what happened
            
            current_task = f"{task}\n\nPlan:\n{plan}"
            
            while iterations_used < max_iterations:
                iterations_used += 1
                if trace:
                    trace.add_step("AutoMode", f"Iteration {iterations_used}/{max_iterations}")

                # Solve (Generate Diff)
                # We append previous errors to current task
                try:
                    diff = engine.run_solve(current_task)
                except Exception as e:
                     if trace: trace.add_step("AutoMode", "Solve failed", status="FAIL", details=str(e))
                     return json.dumps({"success": False, "error": f"Solve error: {e}"})

                if not diff or "+++" not in diff:
                     current_task += "\n\nError: You did not return a valid Unified Diff. Please try again."
                     continue
                
                # Human Check
                if human_check:
                    print(f"\n[AutoMode] Proposed Diff for Iteration {iterations_used}:\n{diff}\n")
                    confirm = input("[AutoMode] Apply this diff? (y/n): ")
                    if confirm.lower() != 'y':
                        if trace: trace.add_step("AutoMode", "User rejected diff", status="SKIPPED")
                        return json.dumps({"success": False, "message": "User aborted."})

                # Apply
                success = DiffApplier.apply_unified_diff(diff)
                if not success:
                    current_task += "\n\nError: Failed to apply the diff. Check file paths and context."
                    if trace: trace.add_step("AutoMode", "Diff application failed", status="FAIL")
                    continue
                
                if trace: trace.add_step("AutoMode", "Diff applied successfully")

                # Validate
                # We assume pytest is the validator. Ideally this should be configurable.
                validation = ShellTools.execute("pytest")
                
                if validation.success:
                    if trace: trace.add_step("AutoMode", "Validation passed")
                    return json.dumps({
                        "success": True,
                        "message": "Feature implemented and verified.",
                        "iterations_used": iterations_used,
                        "artifacts": ["(Check git status)"] # Diffs don't easily tell us new files
                    })
                else:
                    error_msg = f"Tests failed:\n{validation.output[-500:]}" # Last 500 chars
                    current_task += f"\n\nError: Validation Failed:\n{error_msg}\n\nPlease fix the code."
                    if trace: trace.add_step("AutoMode", "Validation failed", status="FAIL", details=error_msg)
            
            return json.dumps({
                "success": False,
                "message": "Max iterations reached without success.",
                "iterations_used": iterations_used
            })

        except Exception as e:
            tb = traceback.format_exc()
            if trace:
                 trace.add_step("AutoMode", "Critical Error", status="FAIL", details=str(e))
            return json.dumps({
                "success": False,
                "error": str(e),
                "traceback": tb
            })
