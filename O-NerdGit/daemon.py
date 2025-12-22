#!/usr/bin/env python3
"""
O Nerd - Sistema de Gerenciamento de Serviço
Roda o O Nerd como um daemon que fica sempre ouvindo (voz ou texto)
"""

import os
import sys
import time
import argparse
from pathlib import Path

try:
    from colorama import init, Fore, Style
    init()
except:
    class Fore:
        GREEN = CYAN = YELLOW = RED = MAGENTA = WHITE = RESET = ""
    class Style:
        BRIGHT = RESET_ALL = ""

# Adiciona o diretório do script ao path
SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SCRIPT_DIR))

from config import GOOGLE_API_KEY, ASSISTANT_NAME
from voice import get_voice_assistant

def print_banner():
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
║              O Nerd virtual do seu sistema!                 ║
║                  Dev Manu o Nerd                            ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}"""
    print(banner)

class OnerdDaemon:
    """Gerencia O Nerd rodando como um serviço em background"""
    
    def __init__(self, text_mode=False):
        self.is_running = False
        self.voice_assistant = None
        self.text_mode = text_mode
        
    def start(self):
        """Inicia o daemon"""
        if not GOOGLE_API_KEY:
            print(f"{Fore.RED}[ERRO] GOOGLE_API_KEY não configurada!{Style.RESET_ALL}")
            return False
        
        self.is_running = True
        print_banner()
        
        if self.text_mode:
            print(f"{Fore.CYAN}[⌨️  ] Iniciando {ASSISTANT_NAME} em MODO TEXTO...{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.CYAN}[🎤] Iniciando {ASSISTANT_NAME} em MODO VOZ...{Style.RESET_ALL}\n")
        
        self.voice_assistant = get_voice_assistant()
        
        print(f"{Fore.GREEN}[OK] {ASSISTANT_NAME} está pronto!{Style.RESET_ALL}")
        
        if self.text_mode:
            print(f"{Fore.YELLOW}[💬] Digite seus comandos abaixo (ou 'sair' para encerrar){Style.RESET_ALL}\n")
            self._listen_loop_text()
        else:
            print(f"{Fore.YELLOW}[🎤] Diga 'O Nerd' ou 'Oi Nerd' para me chamar{Style.RESET_ALL}\n")
            self._listen_loop_voice()
    
    def _listen_loop_text(self):
        """Loop de entrada por texto"""
        while self.is_running:
            try:
                user_input = input(f"{Fore.GREEN}Você: {Style.RESET_ALL}").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ["sair", "exit", "quit"]:
                    self.voice_assistant.speak("Até mais! Encerrando...")
                    self.stop()
                    return
                
                print(f"{Fore.CYAN}[📝] Processando comando...{Style.RESET_ALL}")
                self._process_command(user_input)
                
            except KeyboardInterrupt:
                self.stop()
            except Exception as e:
                print(f"{Fore.YELLOW}[AVISO] Erro: {e}{Style.RESET_ALL}")
                time.sleep(1)
    
    def _listen_loop_voice(self):
        """Loop de entrada por voz"""
        while self.is_running:
            try:
                if self.voice_assistant.is_voice_available():
                    try:
                        print(f"{Fore.CYAN}[🎤] Ouvindo...{Style.RESET_ALL}", end="\r")
                        user_input = self.voice_assistant.listen(timeout=3)
                    except:
                        continue
                    
                    if not user_input:
                        continue
                    
                    text_lower = user_input.lower()
                    print(f"{Fore.MAGENTA}[VOZ] Você disse: {user_input}{Style.RESET_ALL}            ")
                    
                    # Verifica se foi chamado pelo nome
                    if "nerd" in text_lower:
                        command = text_lower.replace("o nerd", "").replace("ó nerd", "").replace("nerd", "").strip()
                        
                        if not command:
                            self.voice_assistant.speak(f"Sim? Como posso ajudar?")
                            continue
                        
                        print(f"{Fore.GREEN}[✓] ATIVADO - Processando comando...{Style.RESET_ALL}")
                        self._process_command(command)
                else:
                    print(f"{Fore.YELLOW}[Aviso] Microfone não disponível. Use modo texto: python daemon.py --text{Style.RESET_ALL}")
                    time.sleep(5)
                        
            except KeyboardInterrupt:
                self.stop()
            except Exception as e:
                print(f"{Fore.YELLOW}[AVISO] Erro: {e}{Style.RESET_ALL}")
                time.sleep(1)
    
    def _process_command(self, user_input):
        """Processa um comando recebido"""
        try:
            from o_nerd import detect_command, handle_command, chat_with_ai
            
            cmd_type, arg = detect_command(user_input)
            
            if cmd_type == "exit":
                self.voice_assistant.speak("Até mais! Desligando...")
                self.stop()
                return
            
            # Processa comando
            if cmd_type:
                result = handle_command(cmd_type, arg)
                if result:
                    print(f"{Fore.CYAN}[O Nerd] {result}{Style.RESET_ALL}")
                    self.voice_assistant.speak(result)
                    time.sleep(0.5)
                return
            
            # Se não é comando, responde com IA
            print(f"{Fore.CYAN}[IA] Consultando Gemini...{Style.RESET_ALL}")
            response = chat_with_ai(user_input)
            print(f"{Fore.CYAN}[O Nerd] {response}{Style.RESET_ALL}")
            self.voice_assistant.speak(response)
            time.sleep(0.5)
            
        except Exception as e:
            print(f"{Fore.RED}[ERRO] {e}{Style.RESET_ALL}")
            try:
                self.voice_assistant.speak("Desculpe, tive um erro ao processar seu comando.")
            except:
                pass
    
    def stop(self):
        """Para o daemon"""
        self.is_running = False
        print(f"\n{Fore.YELLOW}[🛑] {ASSISTANT_NAME} desligando...{Style.RESET_ALL}")
        time.sleep(1)
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="O Nerd - Assistente Virtual")
    parser.add_argument("--text", "-t", action="store_true", help="Ativa modo texto (teclado em vez de voz)")
    parser.add_argument("--voice", "-v", action="store_true", help="Ativa modo voz (padrão)")
    
    args = parser.parse_args()
    
    # Se nenhum modo foi especificado, tenta voz primeiro
    text_mode = args.text
    
    daemon = OnerdDaemon(text_mode=text_mode)
    try:
        daemon.start()
    except KeyboardInterrupt:
        daemon.stop()

