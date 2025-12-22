#!/usr/bin/env python3
"""
Script de teste para validar se a IA está respondendo corretamente
"""

import os
import sys
from config import GOOGLE_API_KEY, ASSISTANT_NAME, SYSTEM_PROMPT
import google.generativeai as genai

print(f"🤖 Testando {ASSISTANT_NAME}...\n")

# Verifica se a chave está configurada
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "":
    print("❌ ERRO: Chave da API não configurada!")
    print("Configure a variável GOOGLE_API_KEY e tente novamente.")
    sys.exit(1)

print(f"✅ Chave da API configurada")

# Tenta conectar com a API
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Teste simples
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=SYSTEM_PROMPT
    )
    
    print("📡 Conectando à API Gemini...")
    response = model.generate_content(
        "Olá! Como você pode me ajudar?",
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=200,
            temperature=0.9
        )
    )
    
    print(f"✅ Conexão com sucesso!\n")
    print(f"{ASSISTANT_NAME}: {response.text}\n")
    
    # Teste de conversação
    print("=" * 60)
    print("🧪 TESTE DE CONVERSAÇÃO")
    print("=" * 60)
    
    conversation = [
        {"role": "user", "parts": ["Qual é a capital do Brasil?"]},
    ]
    
    response = model.generate_content(
        conversation,
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=200,
            temperature=0.9
        )
    )
    
    print(f"Você: Qual é a capital do Brasil?")
    print(f"{ASSISTANT_NAME}: {response.text}\n")
    
    print("=" * 60)
    print("✅ TESTES PASSARAM! O Nerd está funcionando corretamente!")
    print("=" * 60)
    
except Exception as e:
    error_msg = str(e)
    print(f"\n❌ ERRO: {error_msg}\n")
    
    if "quota" in error_msg.lower() or "429" in error_msg:
        print("📌 Seu limite de uso gratuito foi excedido.")
        print("📌 Aguarde 24 horas ou configure uma chave API Premium")
        print("📌 Acesse: https://ai.google.dev/dashboard")
    elif "api_key" in error_msg.lower() or "authentication" in error_msg.lower():
        print("📌 Erro na autenticação da chave API")
        print("📌 Verifique se a chave está correta em config.py")
    
    sys.exit(1)
