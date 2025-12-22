@echo off
REM ============================================
REM  O Nerd - Auto-Iniciar no Startup do Windows
REM ============================================

cd /d "%~dp0"

REM Define a variável de ambiente com a chave
set GOOGLE_API_KEY=AIzaSyB-LMlukCeYQ3fHlGVJiwaKRCCahZ6aJBw

REM Executa o daemon em background
python daemon.py

pause
