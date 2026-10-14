@echo off
title CardioScan AI - FastAPI Production Microservice & Web Interface
echo =========================================================================
echo    CardioScan AI: FastAPI REST Service & Responsive Web App
echo    Machine Learning ^& AI Major Capstone Project (Week 4)
echo    Student: Vivek Vardhan | Submission Date: October 2026
echo =========================================================================
echo.

cd /d "%~dp0"

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=python
) else (
    set PY_CMD="C:\Users\VIVEK VARDHAN\AppData\Local\Python\bin\python.exe"
)

echo Starting FastAPI Server on http://localhost:8000 ...
echo - Web Application: http://localhost:8000/
echo - Interactive Swagger Docs: http://localhost:8000/docs
echo.
%PY_CMD% -m uvicorn api_app:app --host 0.0.0.0 --port 8000 --reload
pause
