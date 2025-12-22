#!/usr/bin/env python3
"""
O Nerd - Modo Texto Puro
========================

Interface limpa e intuitiva para conversas com a IA.
Sem entrada de voz, apenas digitação clara e direta.

Autor: O Nerd Development Team
Versão: 2.0
"""

import os
import sys
from typing import List, Dict, Any

try:
    import google.generativeai as genai
except ImportError:
    print("[ERRO] google-generativeai não instalado. Execute: pip install google-generativeai")
    sys.exit(1)

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    class Fore:
        GREEN = CYAN = YELLOW = RED = MAGENTA = WHITE = RESET = ""
    class Style:
        BRIGHT = RESET_ALL = ""

from config import GOOGLE_API_KEY, ASSISTANT_NAME, SYSTEM_PROMPT


class TextChatInterface:
    """
    Interface de chat em modo texto.
    
    Gerencia a conversa entre usuário e IA através de entrada de texto,
    mantendo histórico de conversa e limitando tamanho para otimizar API.
    """
    
    MAX_HISTORY_SIZE = 20
    MAX_OUTPUT_TOKENS = 1000
    DEFAULT_TEMPERATURE = 0.9
    
    def __init__(self):
        """Inicializa a interface de chat."""
        self.conversation_history: List[Dict[str, Any]] = []
        self.model = None
        self._initialize_api()
    
    def _initialize_api(self) -> None:
        """
        Inicializa a API do Google Generative AI.
        
        Raises:
            SystemExit: Se a chave API não estiver configurada.
        """
        if not GOOGLE_API_KEY:
            print(f"{Fore.RED}[ERRO] Chave API não configurada!{Style.RESET_ALL}")
            print("Configure a variável GOOGLE_API_KEY no arquivo config.py")
            sys.exit(1)
        
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
    
    def _display_banner(self) -> None:
        """Exibe o banner de boas-vindas."""
        banner = f"""
{Fore.CYAN}{Style.BRIGHT}
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║                  {ASSISTANT_NAME} - CHAT MODO TEXTO                ║
║                                                           ║
║                   Digite e converse!                     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""
        print(banner)
    
    def _display_instructions(self) -> None:
        """Exibe as instruções de uso."""
        instructions = f"""
{Fore.YELLOW}📝 Como usar:{Style.RESET_ALL}
  • Digite sua mensagem e pressione ENTER
  • Digite '{Fore.GREEN}sair{Style.RESET_ALL}', '{Fore.GREEN}exit{Style.RESET_ALL}' ou '{Fore.GREEN}quit{Style.RESET_ALL}' para sair
  • O histórico é mantido para conversas mais naturais

{Fore.CYAN}💡 Dica: Você pode fazer perguntas, contar histórias ou pedir ajuda!{Style.RESET_ALL}
"""
        print(instructions)
    
    def _add_to_history(self, role: str, message: str) -> None:
        """
        Adiciona uma mensagem ao histórico.
        
        Args:
            role: "user" ou "model"
            message: Conteúdo da mensagem
        """
        self.conversation_history.append({
            "role": role,
            "parts": [message]
        })
        
        # Mantém apenas as mensagens mais recentes
        if len(self.conversation_history) > self.MAX_HISTORY_SIZE:
            self.conversation_history.pop(0)
            self.conversation_history.pop(0)
    
    def _generate_response(self, user_input: str) -> str:
        """
        Gera resposta da IA.
        
        Args:
            user_input: Mensagem do usuário
            
        Returns:
            Resposta da IA ou mensagem de erro
        """
        try:
            self._add_to_history("user", user_input)
            
            response = self.model.generate_content(
                contents=self.conversation_history,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=self.MAX_OUTPUT_TOKENS,
                    temperature=self.DEFAULT_TEMPERATURE,
                    top_p=0.95,
                    top_k=64
                )
            )
            
            assistant_message = response.text.strip()
            self._add_to_history("model", assistant_message)
            
            return assistant_message
        
        except Exception as error:
            error_message = str(error).lower()
            
            if "quota" in error_message or "429" in error_message:
                return f"{Fore.RED}[ERRO] Quota da API excedida. Aguarde alguns minutos.{Style.RESET_ALL}"
            else:
                return f"{Fore.RED}[ERRO] Não consegui gerar resposta: {str(error)}{Style.RESET_ALL}"
    
    def run(self) -> None:
        """Executa o loop principal da interface de chat."""
        self._display_banner()
        self._display_instructions()
        
        while True:
            try:
                user_input = input(f"{Fore.GREEN}Você: {Style.RESET_ALL}").strip()
                
                # Ignora entrada vazia
                if not user_input:
                    continue
                
                # Verifica comandos de saída
                if user_input.lower() in ["sair", "exit", "quit"]:
                    print(f"\n{Fore.CYAN}Até logo! 👋{Style.RESET_ALL}\n")
                    break
                
                # Gera e exibe resposta
                response = self._generate_response(user_input)
                print(f"{Fore.CYAN}{ASSISTANT_NAME}: {Style.RESET_ALL}{response}\n")
            
            except KeyboardInterrupt:
                print(f"\n\n{Fore.CYAN}Interrompido. Até mais! 👋{Style.RESET_ALL}\n")
                break
            except Exception as error:
                print(f"{Fore.RED}[ERRO] {str(error)}{Style.RESET_ALL}\n")


def main() -> None:
    """Função principal."""
    chat = TextChatInterface()
    chat.run()


if __name__ == "__main__":
    main()
