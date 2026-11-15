@echo off
title Cloud Computing - Wireless Phone Server
cd /d "%~dp0"
echo ===================================================
echo   Starting Wireless Phone Server...
echo ===================================================
python run_phone_server.py
pause
