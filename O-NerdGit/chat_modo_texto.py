#!/usr/bin/env python3
"""
CHAT TEXTO PURO - Modo 100% Interativo
O Nerd em modo texto simples, sem voz
"""

import os
import sys
import google.generativeai as genai
from colorama import init, Fore, Style

from config import GOOGLE_API_KEY, ASSISTANT_NAME, SYSTEM_PROMPT

init()

def show_banner():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}")
    print("╔═══════════════════════════════════════════════════════════╗")
    print(f"║           {ASSISTANT_NAME} - CHAT INTERATIVO              ║")
    print("║                 MODO TEXTO PURO                           ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}✓ Pronto para conversar!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}💬 Digite sua mensagem e pressione ENTER{Style.RESET_ALL}")
    print(f"{Fore.RED}❌ Digite 'sair' para encerrar{Style.RESET_ALL}\n")

def main():
    show_banner()
    
    if not GOOGLE_API_KEY:
        print(f"{Fore.RED}[ERRO] Chave API não configurada!{Style.RESET_ALL}")
        return
    
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
    except Exception as e:
        print(f"{Fore.RED}[ERRO] Falha ao configurar API: {e}{Style.RESET_ALL}")
        return
    
    conversation_history = []
    
    while True:
        try:
            # Input do usuário
            user_input = input(f"{Fore.GREEN}Você:{Style.RESET_ALL} ").strip()
            
            # Verifica se está vazio
            if not user_input:
                print(f"{Fore.YELLOW}[Info] Digite algo!{Style.RESET_ALL}\n")
                continue
            
            # Verifica se é comando de sair
            if user_input.lower() in ["sair", "exit", "quit", "tchau", "adeus"]:
                print(f"\n{Fore.CYAN}👋 Até mais! Foi um prazer conversar com você!{Style.RESET_ALL}\n")
                break
            
            # Adiciona ao histórico
            conversation_history.append({
                "role": "user",
                "parts": [user_input]
            })
            
            # Limita histórico
            if len(conversation_history) > 20:
                conversation_history.pop(0)
                conversation_history.pop(0)
            
            try:
                # Chama a IA
                print(f"{Fore.CYAN}⏳ Pensando...{Style.RESET_ALL}")
                
                model = genai.GenerativeModel(
                    model_name="gemini-2.5-flash",
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
                
                assistant_response = response.text.strip()
                
                # Adiciona resposta ao histórico
                conversation_history.append({
                    "role": "model",
                    "parts": [assistant_response]
                })
                
                # Mostra resposta
                print(f"\n{Fore.CYAN}{ASSISTANT_NAME}:{Style.RESET_ALL} {assistant_response}\n")
                
            except Exception as api_error:
                error_msg = str(api_error)
                
                if "quota" in error_msg.lower() or "429" in error_msg:
                    print(f"\n{Fore.RED}⚠️  Limite de API excedido. Aguarde alguns minutos!{Style.RESET_ALL}\n")
                elif "api_key" in error_msg.lower():
                    print(f"\n{Fore.RED}⚠️  Erro na chave API. Verifique a configuração!{Style.RESET_ALL}\n")
                else:
                    print(f"\n{Fore.RED}⚠️  Erro: {error_msg}{Style.RESET_ALL}\n")
        
        except KeyboardInterrupt:
            print(f"\n\n{Fore.CYAN}👋 Interrompido. Até mais!{Style.RESET_ALL}\n")
            break
        except Exception as e:
            print(f"\n{Fore.RED}[ERRO] {e}{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()
