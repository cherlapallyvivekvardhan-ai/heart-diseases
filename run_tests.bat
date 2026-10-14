@echo off
title CardioScan AI - Automated Test Suite
echo Running automated verification tests...
cd /d "%~dp0"

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=python
) else (
    set PY_CMD="C:\Users\VIVEK VARDHAN\AppData\Local\Python\bin\python.exe"
)

%PY_CMD% test_prediction.py
pause
