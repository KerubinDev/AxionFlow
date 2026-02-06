import typer
import os
import sys
import shutil
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from axion.core.config import load_config, CONFIG_FILE
from axion.core.providers import detect_provider
from axion.core.i18n import t

doctor_app = typer.Typer(help="Diagnose system and configuration issues.")
console = Console()

@doctor_app.callback(invoke_without_command=True)
def run_doctor(ctx: typer.Context):
    """
    Run a health check on the Axion environment.
    """
    if ctx.invoked_subcommand:
        return

    console.print(t("doctor.checking"))
    console.print()

    checks = []
    
    # 1. Python Check
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
    checks.append(("✅" if sys.version_info >= (3, 10) else "❌", t("doctor.python"), py_ver))

    # 2. Dependencies
    has_git = shutil.which("git") is not None
    checks.append(("✅" if has_git else "❌", t("doctor.dependencies"), "git" if has_git else "git missing"))

    # 3. Config Check
    config = load_config()
    conf_status = "✅" if config else "❌"
    conf_msg = str(CONFIG_FILE) if config else t("doctor.fail.config")
    checks.append((conf_status, t("doctor.config"), conf_msg))
    
    # 4. API Key & Connectivity
    api_status = "❌"
    conn_status = "❌"
    conn_msg = "-"
    
    if config:
        model_conf = config.get("model", {})
        key_ref = model_conf.get("api_key", "")
        if key_ref:
             if key_ref.startswith("env:"):
                 env_var = key_ref[4:]
                 val = os.getenv(env_var)
                 if val:
                     api_status = "✅"
                     api_detail = f"Variable {env_var} set"
                 else:
                     api_status = "❌"
                     api_detail = f"Variable {env_var} is EMPTY"
                     conn_msg = t("doctor.fail.key")
             else:
                 api_status = "✅"
                 api_detail = "Direct key configured"
             
             # Connectivity Test
             if api_status == "✅":
                 try:
                     from axion.models.base import get_model
                     try:
                        model = get_model()
                        conn_status = "✅"
                        conn_msg = "OK"
                     except Exception as e:
                        conn_status = "⚠️" 
                        conn_msg = t("doctor.warn.connection")
                        if "api key" in str(e).lower():
                            api_status = "❌"
                            conn_msg = t("doctor.fail.key")
                     
                 except Exception:
                     conn_status = "⚠️"
                     conn_msg = t("doctor.warn.connection")
        else:
             api_status = "❌"
             api_detail = "Missing"
             conn_msg = t("doctor.fail.key")

    checks.append((api_status, t("doctor.key"), api_detail))
    checks.append((conn_status, t("doctor.connection"), conn_msg))

    # Output
    issues = 0
    for icon, label, detail in checks:
        console.print(f"{icon} [bold]{label}[/]: {detail}")
        if icon == "❌": issues += 1
        
    console.print()
    if issues == 0:
        console.print(t("doctor.all_good"))
    else:
        console.print(t("doctor.issues_found"))
