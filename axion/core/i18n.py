from typing import Dict, Any, Optional
from axion.core.config import get_config_value

TRANSLATIONS = {
    "en": {
        "onboarding.welcome": "[bold cyan]Axion Configuration[/]\n\n[italic]API-first setup...[/]",
        "onboarding.api_key_prompt": "🔑 Paste your API Key (or type 'ollama' for local)",
        "onboarding.provider_detected": "[bold green]✅ Detected Provider:[/] {provider}",
        "onboarding.models_consulting": "[bold blue]Consulting {provider} API for available models...",
        "onboarding.models_failed": "[bold red]❌ Failed to list models:[/] {error}",
        "onboarding.no_models": "[bold yellow]⚠️ No models found for this provider.[/]",
        "onboarding.select_model": "\n[bold]Select a model:[/]",
        "onboarding.choice_prompt": "\nChoose a model number",
        "onboarding.invalid_choice": "[bold red]Invalid choice.[/]",
        "onboarding.lang_choice": "🌍 Select preferred UI language (en/pt/es)",
        "onboarding.creativity_prompt": "🎨 Creativity level (0.0=precise, 1.0=creative)",
        "onboarding.env_confirm": "Would you like to use an environment variable for the API key? (Recommended)",
        "onboarding.env_instruction": "[dim]Please ensure you set [bold]{env_var}[/] in your .env or shell.[/]",
        "onboarding.saved": "\n[bold green]✨ Configuration saved![/]",
        "onboarding.saved_location": "\n[dim]Configuration stored at {path}[/]\n",
        
        "solve.thinking": "🤖 [bold green]Thinking...[/]",
        "solve.mode_title": "Solve Mode",
        "solve.trace_title": "[bold cyan]Reasoning Trace[/]",
        "solve.diff_title": "[bold green]Suggested Code Changes (Unified Diff):[/]",
        "solve.interactive_prompt": "\n[A]pprove, [R]efine with feedback, or [C]ancel?",
        "solve.refine_prompt": "Enter your feedback/refinement",
        "solve.cancelled": "[yellow]Operation cancelled.[/]",
        "solve.applying": "[bold yellow]🚀 Applying changes...[/]",
        "solve.success": "[bold green]✅ Changes applied successfully![/]",
        "solve.failed": "[bold red]❌ Failed to apply changes.[/]",
        "solve.discarded": "[bold yellow]Changes discarded.[/]",
        "solve.confirm_apply": "\nDo you want to apply these changes?",
        "solve.input_prompt": "[bold cyan]Describe your task (Ctrl+D to finish):[/]",
        
        "error.solve_failed": "[bold red]Solve failed:[/] {error}",
        "error.validation": "Solve aborted: Model returned invalid content ({type}).",
        
        "config.menu.title": "Configuration Menu",
        "config.menu.option.model": "1. Change Model",
        "config.menu.option.language": "2. Change Language",
        "config.menu.option.show": "3. Show Current Config",
        "config.menu.option.exit": "4. Exit",
        "config.menu.prompt": "Select an option",
        "config.current_title": "Current Configuration",
        
        "welcome.title": "[bold cyan]Welcome to Axion[/]",
        "welcome.subtitle": "A deterministic AI orchestrator for programmers.",
        "welcome.help_hint": "[dim]Run [bold]axion --help[/] to see all commands.[/]",
        "welcome.commands": "[bold]Common Commands:[/]\n- [cyan]axion solve[/]: Solve a coding task\n- [cyan]axion review[/]: Audit current directory\n- [cyan]axion config[/]: Manage settings",

        "doctor.checking": "🩺 Checking system health...",
        "doctor.python": "Python Version",
        "doctor.config": "Configuration File",
        "doctor.key": "API Key",
        "doctor.connection": "API Connectivity",
        "doctor.dependencies": "Dependencies",
        "doctor.warn.connection": "Provider unreachable (Timeout/Rate Limit)",
        "doctor.fail.key": "Missing API Key",
        "doctor.fail.config": "Config missing",
        "doctor.all_good": "[bold green]System Ready![/]",
        "doctor.issues_found": "[bold yellow]Issues found. See above.[/]",

        "solve.input_instruction": "[bold]Input Mode:[/] Type your instructions below.\n[dim]Press [bold]Ctrl+D[/] (or Ctrl+Z on Windows) to send.\nPress [bold]Ctrl+C[/] to cancel.[/]",
        "solve.start_session": "[bold blue]Starting new reasoning session...[/]",
        
        "diff.summary": "[bold]Changes summary:[/]\n- {files} files changed\n- [green]+{insertions}[/] / [red]-{deletions}[/] lines\n",
        
        "error.global_title": "Unexpected Error",
        "error.global_hint": "Run with [bold]--debug[/] or set [bold]AXION_DEBUG=1[/] to see the full traceback.",
    },
    "pt": {
        "onboarding.welcome": "[bold cyan]Configuração do Axion[/]\n\n[italic]Configuração API-first...[/]",
        "onboarding.api_key_prompt": "🔑 Cole sua API Key (ou digite 'ollama' para local)",
        "onboarding.provider_detected": "[bold green]✅ Provedor Detectado:[/] {provider}",
        "onboarding.models_consulting": "[bold blue]Consultando API {provider} para modelos disponíveis...",
        "onboarding.models_failed": "[bold red]❌ Falha ao listar modelos:[/] {error}",
        "onboarding.no_models": "[bold yellow]⚠️ Nenhum modelo encontrado para este provedor.[/]",
        "onboarding.select_model": "\n[bold]Selecione um modelo:[/]",
        "onboarding.choice_prompt": "\nEscolha o número do modelo",
        "onboarding.invalid_choice": "[bold red]Escolha inválida.[/]",
        "onboarding.lang_choice": "🌍 Escolha o idioma da UI (en/pt/es)",
        "onboarding.creativity_prompt": "🎨 Nível de criatividade (0.0=preciso, 1.0=criativo)",
        "onboarding.env_confirm": "Deseja usar uma variável de ambiente para a API key? (Recomendado)",
        "onboarding.env_instruction": "[dim]Por favor, certifique que [bold]{env_var}[/] está definida no seu .env ou shell.[/]",
        "onboarding.saved": "\n[bold green]✨ Configuração salva![/]",
        "onboarding.saved_location": "\n[dim]Configuração salva em {path}[/]\n",
        
        "solve.thinking": "🤖 [bold green]Pensando...[/]",
        "solve.mode_title": "Modo Solução",
        "solve.trace_title": "[bold cyan]Rastro de Racionalização[/]",
        "solve.diff_title": "[bold green]Mudanças Sugeridas (Unified Diff):[/]",
        "solve.interactive_prompt": "\n[A]provar, [R]efinar com feedback, ou [C]ancelar?",
        "solve.refine_prompt": "Digite seu feedback/refinamento",
        "solve.cancelled": "[yellow]Operação cancelada.[/]",
        "solve.applying": "[bold yellow]🚀 Aplicando mudanças...[/]",
        "solve.success": "[bold green]✅ Mudanças aplicadas com sucesso![/]",
        "solve.failed": "[bold red]❌ Falha ao aplicar mudanças.[/]",
        "solve.discarded": "[bold yellow]Mudanças descartadas.[/]",
        "solve.confirm_apply": "\nDeseja aplicar essas mudanças?",
        "solve.input_prompt": "[bold cyan]Descreva sua tarefa (Ctrl+D para finalizar):[/]",
        
        "error.solve_failed": "[bold red]Solução falhou:[/] {error}",
        "error.validation": "Solução abortada: Modelo retornou conteúdo inválido ({type}).",
        
        "config.menu.title": "Menu de Configuração",
        "config.menu.option.model": "1. Alterar Modelo",
        "config.menu.option.language": "2. Alterar Idioma",
        "config.menu.option.show": "3. Mostrar Config Atual",
        "config.menu.option.exit": "4. Sair",
        "config.menu.prompt": "Selecione uma opção",
        "config.current_title": "Configuração Atual",
        
        "welcome.title": "[bold cyan]Bem-vindo ao Axion[/]",
        "welcome.subtitle": "Um orquestrador de IA determinístico para programadores.",
        "welcome.help_hint": "[dim]Execute [bold]axion --help[/] para ver todos os comandos.[/]",
        "welcome.commands": "[bold]Comandos Comuns:[/]\n- [cyan]axion solve[/]: Resolver uma tarefa\n- [cyan]axion review[/]: Auditar diretório\n- [cyan]axion config[/]: Gerenciar configurações",

        "doctor.checking": "🩺 Verificando integridade do sistema...",
        "doctor.python": "Versão Python",
        "doctor.config": "Arquivo de Configuração",
        "doctor.key": "Chave de API",
        "doctor.connection": "Conectividade API",
        "doctor.dependencies": "Dependências",
        "doctor.warn.connection": "Provedor inacessível (Timeout/Rate Limit)",
        "doctor.fail.key": "Chave de API ausente",
        "doctor.fail.config": "Configuração ausente",
        "doctor.all_good": "[bold green]Sistema Pronto![/]",
        "doctor.issues_found": "[bold yellow]Problemas encontrados. Veja acima.[/]",

        "solve.input_instruction": "[bold]Modo de Entrada:[/] Digite suas instruções abaixo.\n[dim]Pressione [bold]Ctrl+D[/] (ou Ctrl+Z no Windows) para enviar.\nPressione [bold]Ctrl+C[/] para cancelar.[/]",
        "solve.start_session": "[bold blue]Iniciando nova sessão de raciocínio...[/]",
        
        "diff.summary": "[bold]Resumo das mudanças:[/]\n- {files} arquivos alterados\n- [green]+{insertions}[/] / [red]-{deletions}[/] linhas\n",

        "error.global_title": "Erro Inesperado",
        "error.global_hint": "Execute com [bold]--debug[/] ou defina [bold]AXION_DEBUG=1[/] para ver o traceback completo.",
    }
}

def t(key: str, **kwargs) -> str:
    """
    Get a translated string for the given key.
    Uses 'model.language' from config, defaulting to 'en'.
    Falls back to 'en' if key is missing in target language.
    """
    lang = get_config_value("model", "language", default="en")
    
    # Support 'es' mapping to 'en' or 'pt' or its own if added later. 
    # For now, let's map unknown langs to 'en'.
    if lang not in TRANSLATIONS:
        lang = "en"
        
    text = TRANSLATIONS.get(lang, {}).get(key)
    
    # Fallback to English
    if text is None:
        text = TRANSLATIONS["en"].get(key, key)
        
    try:
        return text.format(**kwargs)
    except KeyError:
        return text
