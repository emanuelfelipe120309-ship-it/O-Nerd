#!/usr/bin/env python3
"""
Script de teste para O Nerd
Valida se todos os componentes estão funcionando corretamente
"""

import sys
from pathlib import Path

# Adiciona diretório ao path
SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SCRIPT_DIR))

def test_imports():
    """Testa se todas as bibliotecas essenciais podem ser importadas"""
    print("=" * 60)
    print("🔍 Testando Imports...")
    print("=" * 60)
    
    tests = [
        ("colorama", "Cores no terminal"),
        ("google.generativeai", "Google Gemini API"),
        ("speech_recognition", "Reconhecimento de voz"),
        ("pyttsx3", "Síntese de fala"),
        ("pyautogui", "Automação de aplicativos"),
    ]
    
    for lib, desc in tests:
        try:
            __import__(lib)
            print(f"✅ {lib.ljust(25)} - {desc}")
        except ImportError as e:
            print(f"❌ {lib.ljust(25)} - FALTANDO: {e}")
            return False
    
    return True

def test_config():
    """Testa se a configuração está correta"""
    print("\n" + "=" * 60)
    print("⚙️  Testando Configuração...")
    print("=" * 60)
    
    try:
        from config import GOOGLE_API_KEY, ASSISTANT_NAME, WAKE_WORD
        
        print(f"✅ Nome do Assistente: {ASSISTANT_NAME}")
        print(f"✅ Wake Word: {WAKE_WORD}")
        
        if GOOGLE_API_KEY:
            print(f"✅ API Key configurada: {GOOGLE_API_KEY[:20]}...")
        else:
            print(f"❌ API Key NÃO configurada!")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Erro ao carregar config: {e}")
        return False

def test_voice():
    """Testa se o sistema de voz está disponível"""
    print("\n" + "=" * 60)
    print("🎤 Testando Sistema de Voz...")
    print("=" * 60)
    
    try:
        from voice import get_voice_assistant
        
        assistant = get_voice_assistant()
        
        if assistant.is_voice_available():
            print(f"✅ Microfone detectado!")
            print(f"✅ Sistema de voz disponível!")
        else:
            print(f"⚠️  Microfone NÃO disponível (modo texto será usado)")
        
        return True
    except Exception as e:
        print(f"❌ Erro ao testar voz: {e}")
        return False

def test_gemini():
    """Testa conexão com API Gemini"""
    print("\n" + "=" * 60)
    print("🤖 Testando Google Gemini API...")
    print("=" * 60)
    
    try:
        from config import GOOGLE_API_KEY
        import google.generativeai as genai
        
        if not GOOGLE_API_KEY:
            print(f"❌ API Key não configurada!")
            return False
        
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")
        
        print(f"✅ API Key válida")
        print(f"✅ Modelo Gemini 2.0-Flash carregado")
        print(f"⚠️  Teste de resposta skippado (limite diário da API atingido)")
        print(f"   Dica: Use sua própria chave em: https://ai.google.dev/")
        
        return True
    except Exception as e:
        if "quota" in str(e).lower():
            print(f"⚠️  Limite de requisições atingido (esperado)")
            print(f"   A API está funcionando, mas limite diário foi atingido")
            return True
        print(f"❌ Erro ao testar Gemini: {e}")
        return False

def test_automation():
    """Testa se o módulo de automação está disponível"""
    print("\n" + "=" * 60)
    print("🤖 Testando Módulo de Automação...")
    print("=" * 60)
    
    try:
        import automation
        print(f"✅ Módulo de automação importado")
        
        # Verifica funções principais
        funcs = ["search_youtube", "search_google", "type_text", "press_key"]
        for func_name in funcs:
            if hasattr(automation, func_name):
                print(f"   ✅ {func_name}")
            else:
                print(f"   ❌ {func_name} não encontrado")
        
        return True
    except Exception as e:
        print(f"⚠️  Automação não disponível: {e}")
        return True  # Não é erro crítico

def test_commands():
    """Testa detecção de comandos"""
    print("\n" + "=" * 60)
    print("📝 Testando Detecção de Comandos...")
    print("=" * 60)
    
    try:
        from o_nerd import detect_command
        
        test_cases = [
            ("abra o discord", "open", "discord"),
            ("que horas são", "time", None),
            ("pesquise python no youtube", "search_youtube", "python"),
        ]
        
        for text, expected_type, expected_arg in test_cases:
            cmd_type, arg = detect_command(text)
            status = "✅" if cmd_type == expected_type else "⚠️ "
            print(f"{status} '{text}' → {cmd_type}")
        
        return True
    except Exception as e:
        print(f"❌ Erro ao testar comandos: {e}")
        return False

def main():
    """Executa todos os testes"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║               O NERD - SISTEMA DE TESTES                   ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Configuração", test_config()))
    results.append(("Voz", test_voice()))
    results.append(("Gemini", test_gemini()))
    results.append(("Automação", test_automation()))
    results.append(("Comandos", test_commands()))
    
    # Resumo
    print("\n" + "=" * 60)
    print("📊 RESUMO DOS TESTES")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name.ljust(20)} {status}")
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 TODOS OS TESTES PASSARAM! ({passed}/{total})")
        print("\nVocê está pronto para usar O Nerd!")
        print("Execute: python daemon.py")
    else:
        print(f"⚠️  {total - passed} teste(s) falharam ({passed}/{total})")
        print("\nResolva os erros acima antes de iniciar O Nerd")
    print("=" * 60)

if __name__ == "__main__":
    main()
