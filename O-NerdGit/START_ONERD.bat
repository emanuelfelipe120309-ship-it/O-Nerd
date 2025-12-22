@echo off
REM Script completo para instalar e rodar O Nerd com Gemini
REM Corrigido para capturar chave corretamente

setlocal enabledelayedexpansion

cls
echo.
echo ========================================
echo  O NERD - Assistente Virtual
echo  Configuracao Completa com Gemini
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao esta instalado!
    echo Baixe em: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Instala dependencias
echo [INSTALANDO] Dependencias...
pip install -q google-generativeai SpeechRecognition pyttsx3 colorama comtypes pycaw 2>nul
echo [OK] Dependencias instaladas
echo.

REM Pede chave
echo.
echo Digite sua chave Google Gemini:
echo (Obtenha em: https://aistudio.google.com/apikey)
echo.
set /p CHAVE="Chave: "

REM Remove espacos em branco da chave
setlocal enabledelayedexpansion
set "CHAVE=!CHAVE: =!"
set "CHAVE=!CHAVE:	=!"

echo.
if "!CHAVE!"=="" (
    echo [AVISO] Nenhuma chave fornecida. Rodando em modo offline.
    set "CHAVE=none"
) else (
    echo [OK] Chave configurada: !CHAVE:~0,10!...
)

echo.
echo [INICIANDO] O Nerd...
echo.

REM Inicia o assistente com a chave
if "!CHAVE!"=="none" (
    python o_nerd.py
) else (
    cmd /c "set GOOGLE_API_KEY=!CHAVE! && python o_nerd.py"
)

pause

