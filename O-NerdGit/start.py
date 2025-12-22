#!/usr/bin/env python3
"""
O NERD v2.0 - VERSÃO UNIFICADA COMPLETA
Combina chat em modo texto + detecção de comandos + IA completa
"""

import os
import sys
import re

try:
    from colorama import init, Fore, Style
    init()
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    class Fore:
        GREEN = CYAN = YELLOW = RED = MAGENTA = WHITE = RESET = ""
    class Style:
        BRIGHT = RESET_ALL = ""

import google.generativeai as genai

from config import (
    ASSISTANT_NAME, VERSION, DESCRIPTION, WAKE_WORD, GOOGLE_API_KEY, 
    SYSTEM_PROMPT, DANGEROUS_KEYWORDS
)
from commands import execute_command, is_dangerous_command
from voice import get_voice_assistant

try:
    from automation import execute_action
    AUTOMATION_AVAILABLE = True
except ImportError:
    AUTOMATION_AVAILABLE = False
    print("[AVISO] Modulo de automação nao disponivel")

# Configure Google Generative AI (Gemini)
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

conversation_history = []

def print_banner():
    """Mostra o banner de inicialização"""
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     ██████╗     ███╗   ██╗███████╗██████╗ ██████╗            ║
║    ██╔═══██╗    ████╗  ██║██╔════╝██╔══██╗██╔══██╗           ║
║    ██║   ██║    ██╔██╗ ██║█████╗  ██████╔╝██║  ██║           ║
║    ██║   ██║    ██║╚██╗██║██╔══╝  ██╔══██╗██║  ██║           ║
║    ╚██████╔╝    ██║ ╚████║███████╗██║  ██║██████╔╝           ║
║     ╚═════╝     ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═════╝            ║
║                                                              ║
║              {DESCRIPTION.center(38)}              ║
║                  {VERSION.center(32)}                  ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""
    print(banner)

def print_help():
    """Mostra os comandos disponíveis"""
    help_text = f"""
{Fore.YELLOW}╔══ COMANDOS DISPONÍVEIS ══╗{Style.RESET_ALL}

{Fore.GREEN}[NAVEGAÇÃO WEB]{Style.RESET_ALL}
  • "abrir youtube"     - Abre YouTube
  • "abrir google"      - Abre Google
  • "abrir [site]"      - Abre qualquer site

{Fore.GREEN}[PESQUISAS]{Style.RESET_ALL}
  • "pesquisar [algo] no google"   - Pesquisa no Google
  • "pesquisar [algo] no youtube"  - Pesquisa no YouTube

{Fore.GREEN}[APLICATIVOS]{Style.RESET_ALL}
  ✨ TODOS OS SEUS APPS ESTÃO DISPONÍVEIS! ✨
  • "abrir discord"      - Abre Discord
  • "abrir steam"        - Abre Steam
  • "abrir vscode"       - Abre Visual Studio Code
  • "abrir valorant"     - Abre VALORANT
  • "abrir obs"          - Abre OBS Studio
  • "abrir spotify"      - Abre Spotify
  • "abrir calculadora"  - Abre calculadora
  • "abrir notepad"      - Abre bloco de notas
  
  E MUITO MAIS! Você pode abrir qualquer app instalado no seu PC!

{Fore.GREEN}[INFORMAÇÕES]{Style.RESET_ALL}
  • "que horas são"        - Mostra a hora atual
  • "que dia é hoje"       - Mostra a data
  • "informações do sistema" - Detalhes do PC

{Fore.GREEN}[MODOS]{Style.RESET_ALL}
  • "modo voz"   - Ativa entrada por voz
  • "modo texto" - Desativa modo voz

{Fore.GREEN}[OUTROS]{Style.RESET_ALL}
  • "ajuda" ou "help" - Mostra esta mensagem
  • "sair"/"exit"     - Encerra o assistente

{Fore.CYAN}✨ Você também pode conversar NORMALMENTE comigo!{Style.RESET_ALL}
"""
    print(help_text)

def detect_command(user_input):
    """Detecta comandos específicos no texto"""
    from config import WINDOWS_APPS, SAFE_APPS
    text = user_input.lower().strip()
    
    # Comandos de saída
    if any(word in text for word in ["sair", "exit", "quit", "tchau", "adeus", "fechar"]):
        return ("exit", None)
    
    # Ajuda
    if text in ["ajuda", "help", "comandos"]:
        return ("help", None)
    
    # Modo voz
    if "modo voz" in text:
        return ("voice_mode", None)
    
    # Modo texto
    if "modo texto" in text:
        return ("text_mode", None)
    
    # Detecta "abrir [app]" e checa se está na lista de apps
    abrir_match = re.match(r"(?:abrir|abre|abra)\s+(.+)", text)
    if abrir_match:
        app_name = abrir_match.group(1).strip()
        # Verifica se é um app conhecido
        if app_name.lower() in WINDOWS_APPS or app_name.lower() in SAFE_APPS:
            return ("open", app_name)
    
    # Padrões de regex para comandos específicos
    patterns = [
        # Automação: abrir e fazer ação
        (r"abr(?:ir|a)\s+(?:o\s+)?youtube\s+e\s+(?:pesquis|busc)([ae]r?\s+.+)", "youtube_search"),
        (r"abr(?:ir|a)\s+(?:o\s+)?google\s+e\s+(?:pesquis|busc)([ae]r?\s+.+)", "google_search"),
        
        # Detecta "abrir [app]" - prioridade para apps
        (r"(?:abrir|abre|abra|open)\s+(?:o\s+)?(?:aplicativo\s+)?(.+)", "open"),
        (r"pesquisar?\s+(.+?)\s+(?:no\s+)?youtube", "search_youtube"),
        (r"pesquisar?\s+(.+?)\s+(?:no\s+)?google", "search_google"),
        (r"pesquisar?\s+(.+)", "search_google"),
        (r"(?:buscar?|procurar?)\s+(.+?)\s+(?:no\s+)?youtube", "search_youtube"),
        (r"(?:buscar?|procurar?)\s+(.+)", "search_google"),
        (r"(?:que\s+)?hora[s]?\s+(?:são|é|sao)", "time"),
        (r"(?:que\s+)?dia\s+(?:é|e)\s+hoje", "date"),
        (r"(?:data|hoje)", "date"),
        (r"(?:info|informaç(?:ão|ões)|sistema)", "system_info"),
        (r"volume\s+(\d+)", "volume"),
    ]
    
    for pattern, cmd_type in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            arg = match.group(1) if match.lastindex else None
            return (cmd_type, arg)
    
    return (None, None)

def handle_command(cmd_type, arg):
    """Executa comandos específicos"""
    if cmd_type == "youtube_search":
        if AUTOMATION_AVAILABLE:
            import automation
            search_term = arg.replace("pesquisar ", "").replace("pesquisa ", "").replace("buscar ", "").replace("busca ", "").strip()
            automation.search_youtube(search_term)
            return f"Abrindo YouTube e pesquisando por '{search_term}'..."
        else:
            return execute_command("search_youtube", arg)
    
    elif cmd_type == "google_search":
        if AUTOMATION_AVAILABLE:
            import automation
            search_term = arg.replace("pesquisar ", "").replace("pesquisa ", "").replace("buscar ", "").replace("busca ", "").strip()
            automation.search_google(search_term)
            return f"Abrindo Google e pesquisando por '{search_term}'..."
        else:
            return execute_command("search_google", arg)
    
    elif cmd_type == "open":
        from commands import SAFE_APPS, WINDOWS_APPS
        arg_lower = arg.lower() if arg else ""
        
        if arg_lower in WINDOWS_APPS:
            return execute_command("open_app", arg)
        elif arg_lower in SAFE_APPS:
            return execute_command("open_website", arg)
        else:
            result = execute_command("open_app", arg)
            if "Não encontrei" in result or "Erro" in result:
                result = execute_command("open_website", arg)
            return result
    
    elif cmd_type == "search_google":
        return execute_command("search_google", arg)
    
    elif cmd_type == "search_youtube":
        return execute_command("search_youtube", arg)
    
    elif cmd_type == "time":
        return execute_command("get_time", None)
    
    elif cmd_type == "date":
        return execute_command("get_date", None)
    
    elif cmd_type == "system_info":
        return execute_command("get_system_info", None)
    
    elif cmd_type == "volume":
        return execute_command("set_volume", arg)
    
    return None

def chat_with_ai(user_message):
    """Envia mensagem para a IA e recebe resposta"""
    if is_dangerous_command(user_message):
        return "Desculpe, nao posso ajudar com esse tipo de solicitacao por questoes de seguranca. Posso ajudar com outra coisa?"
    
    # Adiciona contexto de hora/dia
    context_msg = user_message
    if any(word in user_message.lower() for word in ["hora", "hoje", "data", "dia"]):
        from commands import get_time, get_date
        context_msg = f"{user_message} [Agora: {get_time()} - {get_date()}]"
    
    conversation_history.append({
        "role": "user",
        "parts": [context_msg]
    })
    
    # Limita histórico
    if len(conversation_history) > 20:
        conversation_history.pop(0)
        conversation_history.pop(0)
    
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
        
        response = model.generate_content(
            contents=conversation_history,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=1000,
                temperature=0.9,
                top_p=0.95,
                top_k=64
            )
        )
        
        assistant_message = response.text.strip()
        
        conversation_history.append({
            "role": "model",
            "parts": [assistant_message]
        })
        
        return assistant_message
        
    except Exception as e:
        error_msg = str(e)
        if "api_key" in error_msg.lower() or "authentication" in error_msg.lower():
            return "[Erro] Erro de autenticacao com a API. Verifique sua chave GOOGLE_API_KEY."
        elif "quota" in error_msg.lower() or "429" in error_msg:
            return "[Erro] Limite de uso da API Gemini excedido. Aguarde alguns minutos!"
        elif "rate" in error_msg.lower():
            return "[Erro] Muitas requisicoes. Aguarde um pouco!"
        print(f"[DEBUG] Erro na IA: {error_msg}")
        return "Ops, tive um problema. Tente novamente!"

def main():
    """Função principal - loop interativo"""
    print_banner()
    
    if not GOOGLE_API_KEY:
        print(f"\n{Fore.RED}[ERRO] A variavel GOOGLE_API_KEY nao esta configurada!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Configure a chave da API Google Gemini antes de iniciar.{Style.RESET_ALL}")
        sys.exit(1)
    
    voice_assistant = get_voice_assistant()
    voice_mode = False
    
    if voice_assistant.is_voice_available():
        print(f"\n{Fore.GREEN}[OK] Microfone detectado! Use 'modo voz' para ativar entrada por voz.{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.YELLOW}[Aviso] Microfone nao disponivel. Usando apenas modo texto.{Style.RESET_ALL}")
    
    voice_assistant.speak(f"Ola! Eu sou {ASSISTANT_NAME}, seu assistente virtual. Como posso ajudar?")
    
    print(f"\n{Fore.CYAN}Digite 'ajuda' para ver os comandos disponiveis.{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Digite 'sair' para encerrar.{Style.RESET_ALL}\n")
    
    while True:
        try:
            if voice_mode and voice_assistant.is_voice_available():
                user_input = voice_assistant.listen()
                if not user_input:
                    continue
                
                text_lower = user_input.lower()
                if WAKE_WORD not in text_lower and "o nerd" not in text_lower:
                    continue
                
                user_input = text_lower.replace("o nerd", "").replace(WAKE_WORD, "").strip()
                if not user_input:
                    voice_assistant.speak("Sim? Como posso ajudar?")
                    continue
            else:
                # MODO TEXTO PURO - ACEITA DIGITAÇÃO
                user_input = input(f"{Fore.GREEN}Você: {Style.RESET_ALL}").strip()
            
            if not user_input:
                continue
            
            # Detecta comandos
            cmd_type, arg = detect_command(user_input)
            
            if cmd_type == "exit":
                voice_assistant.speak("Ate mais! Foi um prazer ajudar voce.")
                print(f"\n{Fore.CYAN}Até mais!{Style.RESET_ALL}\n")
                break
            
            elif cmd_type == "help":
                print_help()
                continue
            
            elif cmd_type == "voice_mode":
                if voice_assistant.is_voice_available():
                    voice_mode = True
                    voice_assistant.speak("Modo de voz ativado! Agora estou ouvindo voce.")
                    print(f"{Fore.GREEN}✓ Modo voz ativado{Style.RESET_ALL}\n")
                else:
                    print(f"{Fore.YELLOW}[Aviso] Microfone nao disponivel.{Style.RESET_ALL}\n")
                continue
            
            elif cmd_type == "text_mode":
                voice_mode = False
                voice_assistant.speak("Modo texto ativado.")
                print(f"{Fore.GREEN}✓ Modo texto ativado{Style.RESET_ALL}\n")
                continue
            
            elif cmd_type:
                # Comando detectado - executa
                result = handle_command(cmd_type, arg)
                if result:
                    voice_assistant.speak(result)
                    print(f"{Fore.CYAN}{ASSISTANT_NAME}: {Style.RESET_ALL}{result}\n")
                    continue
            
            # Nenhum comando específico - responde como IA
            print(f"{Fore.CYAN}⏳ Pensando...{Style.RESET_ALL}")
            response = chat_with_ai(user_input)
            voice_assistant.speak(response)
            print(f"{Fore.CYAN}{ASSISTANT_NAME}: {Style.RESET_ALL}{response}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.CYAN}Interrompido pelo usuario. Ate mais!{Style.RESET_ALL}\n")
            break
        except Exception as e:
            print(f"\n{Fore.RED}[Erro] {e}{Style.RESET_ALL}\n")
            continue

if __name__ == "__main__":
    main()
