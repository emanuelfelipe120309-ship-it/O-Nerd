@echo off
REM ============================================
REM  O Nerd - Modo Texto
REM ============================================

cd /d "%~dp0"

REM Define a variável de ambiente com a chave
set GOOGLE_API_KEY=AIzaSyB-LMlukCeYQ3fHlGVJiwaKRCCahZ6aJBw

REM Executa o daemon em modo texto (teclado)
python daemon.py --text

pause
