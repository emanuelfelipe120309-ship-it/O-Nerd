"""
Módulo de automação de aplicativos
Permite executar ações dentro de programas como digitar, clicar, teclas especiais
"""

import pyautogui
import time
import webbrowser
from typing import List, Dict
import subprocess

# Desabilita falha segura (deixar ligado para segurança)
pyautogui.FAILSAFE = True

def type_text(text: str, interval: float = 0.05):
    """Digita texto caractere por caractere"""
    for char in text:
        pyautogui.typewrite(char, interval=interval)
    time.sleep(0.2)

def press_keys(keys: List[str], delay: float = 0.1):
    """Pressiona múltiplas teclas em sequência"""
    for key in keys:
        pyautogui.press(key)
        time.sleep(delay)

def press_key(key: str):
    """Pressiona uma tecla simples"""
    pyautogui.press(key)
    time.sleep(0.2)

def click(x: int, y: int):
    """Clica em uma posição específica da tela"""
    pyautogui.click(x, y)
    time.sleep(0.3)

def wait(seconds: float = 1.0):
    """Aguarda alguns segundos"""
    time.sleep(seconds)

def search_youtube(query: str):
    """
    Abre YouTube e realiza busca
    Exemplo: search_youtube("células moleculares")
    """
    print(f"[AÇÃO] Abrindo YouTube e buscando: {query}")
    
    # Abre YouTube
    webbrowser.open("https://www.youtube.com")
    wait(3)  # Aguarda página carregar
    
    # Clica na barra de pesquisa (localização comum)
    # Esta é uma abordagem genérica que funciona após carregar
    pyautogui.press('/')  # Atalho para busca no YouTube
    wait(0.5)
    
    # Digita a busca
    pyautogui.typewrite(query, interval=0.05)
    time.sleep(0.5)
    
    # Pressiona Enter para buscar
    pyautogui.press('enter')
    print(f"[✓] Buscando no YouTube por: {query}")

def search_google(query: str):
    """
    Abre Google e realiza busca
    """
    print(f"[AÇÃO] Abrindo Google e buscando: {query}")
    
    webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
    print(f"[✓] Buscando no Google por: {query}")

def open_discord():
    """Abre Discord"""
    print("[AÇÃO] Abrindo Discord...")
    try:
        subprocess.Popen("discord.exe")
        print("[✓] Discord aberto")
    except:
        webbrowser.open("https://discord.com")
        print("[✓] Discord aberto no navegador")

def open_whatsapp():
    """Abre WhatsApp"""
    print("[AÇÃO] Abrindo WhatsApp...")
    try:
        subprocess.Popen("C:\\Program Files\\WhatsApp\\WhatsApp.exe")
        print("[✓] WhatsApp aberto")
    except:
        webbrowser.open("https://web.whatsapp.com")
        print("[✓] WhatsApp Web aberto")

def send_message_whatsapp(contact: str, message: str):
    """
    Envia mensagem no WhatsApp Web
    Nota: Requer que WhatsApp Web já esteja autenticado
    """
    print(f"[AÇÃO] Enviando mensagem para {contact}...")
    
    # Abre WhatsApp Web
    webbrowser.open("https://web.whatsapp.com")
    wait(5)  # Aguarda carregar
    
    # Clica na barra de pesquisa
    pyautogui.hotkey('ctrl', 'f')
    wait(0.5)
    
    # Digita o contato
    pyautogui.typewrite(contact, interval=0.05)
    time.sleep(0.5)
    pyautogui.press('enter')
    wait(1)
    
    # Clica no campo de mensagem
    # Posição aproximada - pode variar conforme resolução
    pyautogui.press('tab')
    time.sleep(0.3)
    
    # Digita mensagem
    pyautogui.typewrite(message, interval=0.02)
    time.sleep(0.5)
    
    # Envia
    pyautogui.hotkey('ctrl', 'enter')
    print(f"[✓] Mensagem enviada para {contact}")

def type_email(email: str):
    """Digita um email de forma segura (lida com @)"""
    import pyperclip
    
    # Usa clipboard para colar (melhor que digitar @)
    try:
        pyperclip.copy(email)
        pyautogui.hotkey('ctrl', 'v')
    except:
        # Fallback para digitação manual
        pyautogui.typewrite(email.replace('@', 'ARROBA'), interval=0.05)

# Dicionário de ações automáticas
AUTOMATION_ACTIONS = {
    "youtube": search_youtube,
    "pesquisar no youtube": search_youtube,
    "google": search_google,
    "pesquisar": search_google,
    "discord": open_discord,
    "whatsapp": open_whatsapp,
}

def execute_action(action_name: str, *args):
    """Executa uma ação de automação"""
    action_lower = action_name.lower()
    
    for key, func in AUTOMATION_ACTIONS.items():
        if key in action_lower:
            try:
                if args:
                    func(args[0])
                else:
                    func()
                return True
            except Exception as e:
                print(f"[ERRO] Falha ao executar {action_name}: {e}")
                return False
    
    return False

if __name__ == "__main__":
    # Teste
    print("Módulo de automação carregado com sucesso")
