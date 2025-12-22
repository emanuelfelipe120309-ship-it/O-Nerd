#!/usr/bin/env python3
"""
Script para configurar a chave da API Google Gemini
Gera uma nova chave gratuita automaticamente
"""

import os
import webbrowser
import time

print("""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║          🔧 CONFIGURADOR DE API - O NERD v2.0                ║
║                                                                ║
║          Vamos configurar uma chave de API nova!             ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
""")

print("""
⚠️  SUA CHAVE ATUAL ESTÁ INVÁLIDA OU EXPIROU!

Para usar O Nerd, você precisa de uma chave API do Google Gemini.
A boa notícia: A PRIMEIRA é 100% GRATUITA! 🎉

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OPÇÃO 1 - AUTOMÁTICA (Recomendado):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Vou abrir o site para você gerar a chave automaticamente.
Siga estes passos:

1. Clique no botão "Get API Key" (azul)
2. Selecione "Create API key in new project" 
3. Copie a chave gerada
4. Cole aqui no terminal quando pedir

Abrindo o site... ⏳
""")

time.sleep(2)

# Abre o site de API key
webbrowser.open("https://aistudio.google.com/app/apikey")

print("\n✓ Site aberto no navegador!")
print("Aguarde carregar e clique em 'Get API Key'...\n")

time.sleep(3)

# Solicita a chave
while True:
    api_key = input("Cole sua chave de API aqui: ").strip()
    
    if not api_key:
        print("❌ Chave vazia! Tente novamente.")
        continue
    
    if len(api_key) < 20:
        print("❌ Chave muito curta. Verifique se copiou corretamente.")
        continue
    
    break

print(f"\n✓ Chave recebida: {api_key[:20]}...")
print("Salvando configuração...")

# Salva no config.py
config_path = os.path.join(os.path.dirname(__file__), "config.py")

try:
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Substitui a chave antiga pela nova
    old_key_pattern = 'GOOGLE_API_KEY = "AIzaSyBLtuKHpPKIbM7iKdpj8T9k-IbuK4fQdDE"'
    new_key_pattern = f'GOOGLE_API_KEY = "{api_key}"'
    
    # Se não encontrar a chave antiga, tenta substituir qualquer chave
    if old_key_pattern in content:
        content = content.replace(old_key_pattern, new_key_pattern)
    else:
        # Tenta encontrar qualquer linha com GOOGLE_API_KEY hardcoded
        import re
        pattern = r'GOOGLE_API_KEY = "AIzaSy[^"]*"'
        content = re.sub(pattern, new_key_pattern, content)
    
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("✓ Configuração salva com sucesso!")
    
except Exception as e:
    print(f"❌ Erro ao salvar: {e}")
    print("\nAlternativa: Configure a variável de ambiente manualmente")
    print(f"No PowerShell execute:")
    print(f'$env:GOOGLE_API_KEY = "{api_key}"')
    exit(1)

print("""
╔════════════════════════════════════════════════════════════════╗
║                  ✅ CONFIGURAÇÃO COMPLETA!                    ║
╚════════════════════════════════════════════════════════════════╝

Próximo passo: Inicie O Nerd novamente!

   python start.py

Sua chave de API foi configurada com sucesso! 🎉
""")
