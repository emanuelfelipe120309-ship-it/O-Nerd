"""
O Nerd - Módulo de Comandos
============================

Executa comandos do sistema como abrir aplicativos, sites, etc.
Inclui validação de segurança para evitar comandos perigosos.

Autor: O Nerd Development Team
Versão: 2.0
"""

import subprocess
import webbrowser
import platform
import datetime
import os
from typing import Optional
from config import SAFE_APPS, WINDOWS_APPS, DANGEROUS_KEYWORDS


def is_dangerous_command(text: str) -> bool:
    """
    Verifica se um comando contém palavras-chave perigosas.
    
    Args:
        text: Texto do comando a verificar
        
    Returns:
        True se o comando é perigoso, False caso contrário
    """
    text_lower = text.lower()
    for keyword in DANGEROUS_KEYWORDS:
        if keyword in text_lower:
            return True
    return False


def open_website(site_name: str) -> str:
    """
    Abre um website no navegador padrão.
    
    Args:
        site_name: Nome do site ou URL
        
    Returns:
        Mensagem de confirmação
    """
    site_name_lower = site_name.lower().strip()
    
    # Verifica se é um site conhecido e seguro
    if site_name_lower in SAFE_APPS:
        url = SAFE_APPS[site_name_lower]
        webbrowser.open(url)
        return f"Abrindo {site_name}..."
    
    # Se começa com http, abre direto
    if site_name_lower.startswith("http"):
        webbrowser.open(site_name_lower)
        return f"Abrindo {site_name_lower}..."
    
    # Assume que é um domínio e adiciona .com
    url = f"https://www.{site_name_lower}.com"
    webbrowser.open(url)
    return f"Tentando abrir {url}..."


def open_app(app_name: str) -> str:
    """
    Abre um aplicativo do Windows.
    
    Args:
        app_name: Nome do aplicativo a abrir
        
    Returns:
        Mensagem de status ou erro
    """
    app_name_lower = app_name.lower().strip()
    
    if app_name_lower in WINDOWS_APPS:
        app_command = WINDOWS_APPS[app_name_lower]
        try:
            if app_command.startswith("ms-"):
                os.startfile(app_command)
            else:
                subprocess.Popen(app_command, shell=True)
            return f"Abrindo {app_name}..."
        except Exception as error:
            return f"Não consegui abrir {app_name}. Erro: {str(error)}"
    
    # Tenta abrir como comando direto
    try:
        subprocess.Popen(app_name_lower, shell=True)
        return f"Tentando abrir {app_name}..."
    except Exception:
        return f"Não encontrei o aplicativo '{app_name}'. Verifique se está instalado."


def search_google(query: str) -> str:
    """
    Realiza busca no Google.
    
    Args:
        query: Termo de busca
        
    Returns:
        Mensagem de confirmação
    """
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Pesquisando por '{query}' no Google..."


def search_youtube(query: str) -> str:
    """
    Realiza busca no YouTube.
    
    Args:
        query: Termo de busca
        
    Returns:
        Mensagem de confirmação
    """
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Pesquisando por '{query}' no YouTube..."


def get_time() -> str:
    """
    Retorna a hora atual.
    
    Returns:
        String com a hora formatada
    """
    now = datetime.datetime.now()
    return f"Agora são {now.strftime('%H:%M')} horas."


def get_date() -> str:
    """
    Retorna a data atual em português.
    
    Returns:
        String com a data formatada
    """
    now = datetime.datetime.now()
    
    dias_semana = [
        'segunda-feira', 'terça-feira', 'quarta-feira',
        'quinta-feira', 'sexta-feira', 'sábado', 'domingo'
    ]
    
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    
    dia_semana = dias_semana[now.weekday()]
    mes = meses[now.month - 1]
    
    return f"Hoje é {dia_semana}, {now.day} de {mes} de {now.year}."


def get_system_info() -> str:
    """
    Retorna informações do sistema.
    
    Returns:
        String com detalhes do PC
    """
    info = [
        f"🖥️  Sistema: {platform.system()} {platform.release()}",
        f"📦 Versão: {platform.version()}",
        f"⚙️  Máquina: {platform.machine()}",
        f"🔧 Processador: {platform.processor()}",
        f"💻 Nome do PC: {platform.node()}",
    ]
    
    return "\n".join(info)


def set_volume(level: int) -> str:
    """
    Ajusta o volume do sistema.
    
    Args:
        level: Nível de volume (0-100)
        
    Returns:
        Mensagem de confirmação ou erro
    """
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        
        volume.SetMasterVolumeLevelScalar(level / 100, None)
        return f"🔊 Volume ajustado para {level}%"
    
    except ImportError:
        return "Para controlar o volume, instale: pip install pycaw comtypes"
    except Exception as error:
        return f"Não consegui ajustar o volume. Erro: {str(error)}"


def execute_command(command_type: str, args: Optional[str] = None) -> Optional[str]:
    """
    Executa um comando especificado.
    
    Args:
        command_type: Tipo de comando a executar
        args: Argumentos do comando
        
    Returns:
        Resultado da execução ou None se comando inválido
    """
    # Verifica segurança antes de executar
    if is_dangerous_command(str(args)):
        return "❌ Desculpe, não posso executar esse comando por questões de segurança."
    
    commands = {
        "open_website": lambda: open_website(args),
        "open_app": lambda: open_app(args),
        "search_google": lambda: search_google(args),
        "search_youtube": lambda: search_youtube(args),
        "get_time": lambda: get_time(),
        "get_date": lambda: get_date(),
        "get_system_info": lambda: get_system_info(),
        "set_volume": lambda: set_volume(int(args) if args else 50),
    }
    
    if command_type in commands:
        return commands[command_type]()
    
    return None
