#!/usr/bin/env python3
"""
Script de teste para verificar se o Gemini está configurado corretamente.
Execute: python test_gemini.py
"""

import os
import sys

# Verifica variável de ambiente
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("❌ ERRO: GOOGLE_API_KEY não configurada!")
    print("\nPara configurar, abra PowerShell e execute:")
    print('$env:GOOGLE_API_KEY="sua_chave_aqui"')
    sys.exit(1)

print("✅ GOOGLE_API_KEY encontrada!")
print(f"Chave: {GOOGLE_API_KEY[:10]}...{GOOGLE_API_KEY[-10:]}")

# Testa importação do google.generativeai
try:
    import google.generativeai as genai
    print("✅ google-generativeai importado com sucesso!")
except ImportError as e:
    print(f"❌ ERRO ao importar google-generativeai: {e}")
    print("Execute: pip install google-generativeai")
    sys.exit(1)

# Testa configuração da API
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    print("✅ API Gemini configurada com sucesso!")
except Exception as e:
    print(f"❌ ERRO ao configurar API: {e}")
    sys.exit(1)

# Testa modelo
try:
    model = genai.GenerativeModel("gemini-2.0-flash")
    print("✅ Modelo Gemini-2.0-Flash disponível!")
except Exception as e:
    print(f"❌ ERRO ao carregar modelo: {e}")
    sys.exit(1)

# Testa resposta
try:
    print("\n🤖 Testando resposta do Gemini...")
    response = model.generate_content("Diga 'Oi, estou funcionando!' em uma única linha.")
    print(f"✅ Resposta: {response.text}")
except Exception as e:
    print(f"❌ ERRO ao gerar resposta: {e}")
    sys.exit(1)

print("\n" + "="*60)
print("🎉 TUDO OK! O Gemini está configurado e funcionando!")
print("="*60)
print("\nAgora execute: python o_nerd.py")
