#!/usr/bin/env python3
"""
Script para detectar todos os apps instalados no Windows
e adicionar automaticamente à lista de apps que O Nerd pode abrir
"""

import os
import subprocess
import sys
from pathlib import Path

print("""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║      🔍 SCANNER DE APLICATIVOS - O NERD v2.0                 ║
║                                                                ║
║    Detectando todos os apps instalados no seu Windows...     ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
""")

def get_installed_apps():
    """Detecta todos os programas instalados no Windows"""
    apps = {}
    
    print("⏳ Procurando em Program Files...")
    
    # Program Files (64-bit)
    program_files = Path("C:\\Program Files")
    if program_files.exists():
        for item in program_files.iterdir():
            if item.is_dir():
                app_name = item.name
                exe_files = list(item.glob("*.exe")) + list(item.glob("*/*.exe"))
                if exe_files:
                    exe_path = str(exe_files[0])
                    apps[app_name.lower()] = exe_path
    
    # Program Files (32-bit)
    print("⏳ Procurando em Program Files (x86)...")
    program_files_x86 = Path("C:\\Program Files (x86)")
    if program_files_x86.exists():
        for item in program_files_x86.iterdir():
            if item.is_dir():
                app_name = item.name
                exe_files = list(item.glob("*.exe")) + list(item.glob("*/*.exe"))
                if exe_files:
                    exe_path = str(exe_files[0])
                    if app_name.lower() not in apps:
                        apps[app_name.lower()] = exe_path
    
    # AppData/Local (aplicativos portáteis)
    print("⏳ Procurando em AppData...")
    appdata = Path(os.path.expanduser("~\\AppData\\Local"))
    if appdata.exists():
        for item in appdata.iterdir():
            if item.is_dir() and item.name not in ["Temp", "Cache"]:
                app_name = item.name
                exe_files = list(item.glob("*.exe")) + list(item.glob("*/*.exe"))
                if exe_files:
                    exe_path = str(exe_files[0])
                    if app_name.lower() not in apps:
                        apps[app_name.lower()] = exe_path
    
    return apps

def get_registry_apps():
    """Detecta apps via Windows Registry (mais confiável)"""
    apps = {}
    
    print("⏳ Procurando no Windows Registry...")
    
    try:
        import winreg
        
        # HKLM - Local Machine (todos os usuários)
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall"
        
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
            for i in range(winreg.QueryInfoKey(key)[0]):
                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)
                
                try:
                    display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    
                    # Tenta encontrar o caminho do executável
                    try:
                        install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                        if install_location:
                            exe_files = list(Path(install_location).glob("*.exe"))
                            if exe_files:
                                apps[display_name.lower()] = str(exe_files[0])
                    except:
                        pass
                except:
                    pass
                finally:
                    winreg.CloseKey(subkey)
        except:
            pass
        finally:
            winreg.CloseKey(key)
    except ImportError:
        print("⚠️  winreg não disponível")
    
    return apps

# Detecta apps
print("\n🔍 Analisando seu sistema...\n")
apps = get_installed_apps()
registry_apps = get_registry_apps()

# Combina resultados
all_apps = {**apps, **registry_apps}

# Remove duplicatas e apps do sistema
excluded = ["windows", "system", "temp", "cache", "service", "update", "driver"]
filtered_apps = {
    name: path for name, path in all_apps.items()
    if not any(excl in name.lower() for excl in excluded)
    and len(name) > 2  # Remove entradas muito curtas
}

print(f"\n✅ Encontrados {len(filtered_apps)} aplicativos!\n")

# Cria dicionário formatado
apps_dict = {}
for name, path in sorted(filtered_apps.items())[:100]:  # Limita a 100 para não ficar muito grande
    # Normaliza nomes
    friendly_name = name.split()[0].lower()  # Pega primeira palavra
    if friendly_name not in apps_dict:  # Evita duplicatas
        apps_dict[friendly_name] = path

print("📋 Apps encontrados (primeiros 50):\n")
for i, (name, path) in enumerate(list(apps_dict.items())[:50]):
    print(f"{i+1:2d}. {name:30s} -> {path[:50]}...")

# Salva em arquivo temporário
output_file = "apps_detected.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for name, path in apps_dict.items():
        f.write(f'    "{name}": "{path}",\n')

print(f"\n✅ Arquivo '{output_file}' criado com sucesso!")
print(f"   Contém {len(apps_dict)} aplicativos prontos para usar.\n")

print("""
PRÓXIMAS ETAPAS:

1. Abra 'config.py' em um editor
2. Procure por 'WINDOWS_APPS = {'
3. Copie o conteúdo de 'apps_detected.txt' 
4. Cole dentro do dicionário WINDOWS_APPS
5. Salve o arquivo

Agora você poderá abrir QUALQUER app por voz ou texto! 🎉
""")

print("\nExemplos de como usar:\n")
print('  "Abra notepad"')
print('  "Abra spotify"')
print('  "Abra discord"')
print('  "Abra chrome"')
print("\nTudo funcionará perfeitamente! ✨\n")
