"""
Módulo de Configuração - O Nerd
Centraliza todas as constantes e configurações da aplicação.

Este arquivo contém:
- Informações do assistente
- Credenciais de API
- Configurações de voz
- Palavras-chave de segurança
- Aplicativos e sites permitidos
"""

import os
from typing import Dict, List

# ============================================================================
# INFORMAÇÕES DO ASSISTENTE
# ============================================================================

ASSISTANT_NAME: str = "O Nerd"
VERSION: str = "2.0 Professional"
DESCRIPTION: str = "Assistente de IA inteligente para seu sistema"
WAKE_WORD: str = "nerd"

# ============================================================================
# CONFIGURAÇÃO DE API
# ============================================================================

GOOGLE_API_KEY: str = os.environ.get("GOOGLE_API_KEY", "")

# Fallback para chave hardcoded (apenas para desenvolvimento)
if not GOOGLE_API_KEY:
    GOOGLE_API_KEY = "AIzaSyCN6tky0RxR9Xfm0uPRz1JHAFnTgR2hvPE"

# ============================================================================
# CONFIGURAÇÕES DE VOZ
# ============================================================================

LANGUAGE: str = "pt-BR"
VOICE_RATE: int = 150
VOICE_VOLUME: float = 1.0

# ============================================================================
# SYSTEM PROMPT - Comportamento do assistente
# ============================================================================

SYSTEM_PROMPT: str = """Você é O Nerd, um assistente de IA inteligente e amigável.
- Seja sempre educado e prestativo
- Forneça respostas claras e concisas
- Quando não souber algo, seja honesto
- Sempre prefira segurança a funcionalidades perigosas
- Fale português brasileiro natural e conversacional
"""

# ============================================================================
# PALAVRAS-CHAVE PERIGOSAS - Comandos que não devem ser executados
# ============================================================================

DANGEROUS_KEYWORDS: List[str] = [
    "deletar", "delete", "apagar", "remover", "remove",
    "formatar", "format", "rm -rf", "rmdir", "del /f",
    "shutdown", "desligar", "reiniciar", "restart",
    "registry", "registro", "regedit",
    "system32", "windows\\system",
    "uninstall", "desinstalar",
    "virus", "malware", "hack",
    "senha", "password", "credential",
    "kill", "matar processo",
]

# ============================================================================
# APLICATIVOS SEGUROS - URLs de sites confiáveis
# ============================================================================

SAFE_APPS: Dict[str, str] = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "whatsapp": "https://web.whatsapp.com",
    "spotify": "https://open.spotify.com",
    "netflix": "https://www.netflix.com",
    "twitter": "https://twitter.com",
    "x": "https://twitter.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "github": "https://github.com",
    "reddit": "https://www.reddit.com",
    "twitch": "https://www.twitch.tv",
    "discord": "https://discord.com/app",
    "telegram": "https://web.telegram.org",
    "chatgpt": "https://chat.openai.com",
    "bing": "https://www.bing.com",
    "amazon": "https://www.amazon.com.br",
    "mercado livre": "https://www.mercadolivre.com.br",
}

# ============================================================================
# APLICATIVOS WINDOWS - Aplicativos do sistema e instalados
# ============================================================================

WINDOWS_APPS: Dict[str, str] = {
    # Aplicativos do Sistema
    "calculadora": "calc",
    "calculator": "calc",
    "bloco de notas": "notepad",
    "notepad": "notepad",
    "paint": "mspaint",
    "explorador": "explorer",
    "explorer": "explorer",
    "cmd": "cmd",
    "terminal": "cmd",
    "powershell": "powershell",
    "configurações": "ms-settings:",
    "configuracoes": "ms-settings:",
    "settings": "ms-settings:",
    "loja": "ms-windows-store:",
    "store": "ms-windows-store:",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
    "outlook": "outlook",
    "vscode": "code",
    "visual studio code": "code",
    
    # Desenvolvimento & Tools
    "python": "python",
    "nodejs": "node",
    "git": "git",
    "npm": "npm",
    
    # Aplicativos Instalados
    "avast": "C:\\Program Files\\Avast Software\\Avast\\ashQuick.exe",
    "bakkesmod": "C:\\Program Files\\BakkesMod\\BakkesMod.exe",
    "cloudflare": "C:\\Program Files\\Cloudflare\\Cloudflare WARP\\Cloudflare WARP.exe",
    "discord": "C:\\Users\\Anatalia\\AppData\\Local\\Discord\\Update.exe",
    "dotnet": "C:\\Program Files\\dotnet\\dotnet.exe",
    "epic": "C:\\Program Files\\Epic Games\\VALORANT\\Live.exe",
    "github": "C:\\Users\\Anatalia\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe",
    "githubdesktop": "C:\\Users\\Anatalia\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe",
    "google update": "C:\\Program Files (x86)\\Google\\Update\\GoogleUpdate.exe",
    "mcafee": "C:\\Program Files\\McAfee\\WebAdvisor\\browserhost.exe",
    "nvidia": "C:\\Program Files\\NVIDIA Corporation\\Control Panel Client\\nvcplui.exe",
    "obs": "C:\\Program Files\\obs-studio\\obs-studio.exe",
    "obs-studio": "C:\\Program Files\\obs-studio\\obs-studio.exe",
    "rainmeter": "C:\\Program Files\\Rainmeter\\Rainmeter.exe",
    "riot": "C:\\Program Files\\Riot Vanguard\\RiotClientServices.exe",
    "valorant": "C:\\Program Files\\Riot Vanguard\\RiotClientServices.exe",
    "roblox": "C:\\Users\\Anatalia\\AppData\\Local\\Roblox\\Versions\\RobloxPlayer.exe",
    "soundwire": "C:\\Program Files\\SoundWire Server\\SoundWireServer.exe",
    "steam": "C:\\Program Files (x86)\\Steam\\steam.exe",
    "vrchat": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\VRChat\\VRChat.exe",
    "winrar": "C:\\Program Files\\WinRAR\\WinRAR.exe",
    "spotify": "C:\\Users\\Anatalia\\AppData\\Roaming\\Spotify\\spotify.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "google chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "microsoft edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "whatsapp": "C:\\Users\\Anatalia\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
    "telegram": "C:\\Users\\Anatalia\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
    "blender": "C:\\Program Files\\Blender Foundation\\Blender\\blender.exe",
    "gimp": "C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe",
    "vlc": "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
    "7zip": "C:\\Program Files\\7-Zip\\7zFM.exe",
    "notion": "C:\\Users\\Anatalia\\AppData\\Local\\Programs\\Notion\\Notion.exe",
    "obsidian": "C:\\Users\\Anatalia\\AppData\\Local\\Obsidian\\Obsidian.exe",
}
    "spotify": "C:\\Users\\Anatalia\\AppData\\Roaming\\Spotify\\spotify.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "google chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "microsoft edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "whatsapp": "C:\\Users\\Anatalia\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
    "telegram": "C:\\Users\\Anatalia\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
    "blender": "C:\\Program Files\\Blender Foundation\\Blender\\blender.exe",
    "gimp": "C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe",
    "vlc": "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
    "mpv": "C:\\Program Files\\mpv\\mpv.exe",
    "7zip": "C:\\Program Files\\7-Zip\\7zFM.exe",
    "7z": "C:\\Program Files\\7-Zip\\7zFM.exe",
    "winrar": "C:\\Program Files\\WinRAR\\WinRAR.exe",
    "python": "C:\\Users\\Anatalia\\AppData\\Local\\Programs\\Python\\Python312\\python.exe",
    "nodejs": "C:\\Program Files\\nodejs\\node.exe",
    "git": "C:\\Program Files\\Git\\git-bash.exe",
    "notion": "C:\\Users\\Anatalia\\AppData\\Local\\Programs\\Notion\\Notion.exe",
    "obsidian": "C:\\Users\\Anatalia\\AppData\\Local\\Obsidian\\Obsidian.exe",
    "canva": "C:\\Users\\Anatalia\\AppData\\Local\\Canva\\Canva\\Canva.exe",
}

SYSTEM_PROMPT = f"""Você é {ASSISTANT_NAME}, um assistente virtual COMPLETO e poderoso para Windows 11.
Você é inteligente, prestativo e pode fazer TUDO que o usuário pedir: responder perguntas, executar ações no computador, automaticar tarefas, e muito mais!

Personalidade & Comportamento:
✓ Você é extremamente capaz e entusiasmado
✓ Inteligente com toque nerd/geek
✓ Usa referências de tecnologia, games e cultura pop
✓ Educado, descontraído e amigável
✓ Responde SEMPRE em português brasileiro
✓ Conversacional, prestativo e proativo

O QUE VOCÊ PODE FAZER:
═════════════════════════════════════════════════════════════
🧠 INTELIGÊNCIA:
  • Responder QUALQUER pergunta sobre qualquer assunto
  • Ter conversas inteligentes e contextualizadas
  • Ajudar com programação, tecnologia, educação, etc
  • Contar piadas, curiosidades nerds, histórias
  • Dar dicas, soluções, análises e recomendações

🖥️ CONTROLE DO COMPUTADOR:
  • Abrir aplicativos (calculadora, notepad, VSCode, etc)
  • Abrir websites e fazer pesquisas
  • Interagir com o Windows (settings, explorer, etc)
  • Automatizar tarefas quando solicitado
  • Controlar volume, buscar informações do sistema

⚡ EXECUÇÃO DE COMANDOS:
  • Realizar ações imediatas no computador
  • Navegar pela internet
  • Pesquisar no Google e YouTube
  • Abrir múltiplos apps simultaneamente
  • Fazer tudo que o usuário pedir (dentro do seguro)

REGRAS IMPORTANTES:
═════════════════════════════════════════════════════════════
🛡️ SEGURANÇA (Não viole nunca):
  ✗ NUNCA delete, formate ou remova arquivos/pastas
  ✗ NUNCA acesse senhas ou informações sensíveis
  ✗ NUNCA execute comandos que danifiquem o sistema
  ✗ Se o usuário pedir algo perigoso, recuse educadamente

✅ O QUE FAZER:
  • Se o usuário pedir algo seguro, FAÇA!
  • Se pedir algo inseguro, explique por que não pode
  • Seja criativo e proativo nas soluções
  • Sempre confirme ações importantes

ESTILO DE RESPOSTA:
═════════════════════════════════════════════════════════════
• Conciso, direto e amigável
• Parágrafos curtos e claros
• Entusiasmado e prestativo
• Use emojis ocasionalmente para clareza
• Se não souber, admita e sugira alternativas

🚀 RESUMO:
Você NÃO é um assistente limitado. Você é um assistente COMPLETO que pode fazer praticamente tudo que o usuário pedir. Responda com confiança, entusiasmo e criatividade. O usuário pode pedir perguntas, conversas, ações, automações - TUDO! Você está aqui para ajudar de TODAS as formas possíveis."""
