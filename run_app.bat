@echo off
title CardioScan AI - Streamlit Web Application
echo =========================================================================
echo    CardioScan AI: Heart Disease Risk Prediction System
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

echo Starting Streamlit Web Application on http://localhost:8501 ...
%PY_CMD% -m streamlit run app.py --server.port 8501
pause
