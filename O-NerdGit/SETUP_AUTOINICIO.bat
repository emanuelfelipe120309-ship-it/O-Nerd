@echo off
REM Script para registrar O Nerd no startup do Windows
REM Execute este arquivo como Administrador

echo.
echo ============================================
echo  O Nerd - Configurar Auto-Startup
echo ============================================
echo.

REM Obtém o caminho do script
set SCRIPT_PATH=%~dp0

REM Cria um arquivo VBS para executar o O Nerd minimizado em background
set VBS_FILE=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\OnerdDaemon.vbs

echo Creating launcher script...

(
    echo ' Auto-iniciar O Nerd Daemon
    echo Set objShell = CreateObject("WScript.Shell"^)
    echo objShell.Run "%SCRIPT_PATH%run_daemon.bat", 0
) > "%VBS_FILE%"

echo.
echo [OK] O Nerd foi configurado para iniciar automaticamente!
echo.
echo Configuração completa:
echo  - Local: %VBS_FILE%
echo  - Arquivo: OnerdDaemon.vbs
echo.
echo Como usar:
echo  1. O Nerd iniciara automaticamente quando voce ligar o computador
echo  2. Diga "O Nerd, [comando]" para ativa-lo
echo     Exemplos:
echo     - "O Nerd, abra o Discord"
echo     - "O Nerd, pesquise sobre inteligencia artificial no YouTube"
echo     - "O Nerd, que horas sao"
echo.
echo  3. O assistente estara SEMPRE OUVINDO em background
echo.
pause

