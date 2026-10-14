@echo off
title CardioScan AI - Ultra-Fast Public Internet Deployment Tunnel
echo =========================================================================
echo    CardioScan AI: Ultra-Fast Public Web Deployment
echo    High-Throughput Vectorized Inference Server + Cloudflare Tunnel
echo =========================================================================
echo.

cd /d "%~dp0"

echo Ensuring High-Speed FastAPI server is running on port 8000...
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=python
) else (
    set PY_CMD="C:\Users\VIVEK VARDHAN\AppData\Local\Python\bin\python.exe"
)

start "" %PY_CMD% -m uvicorn api_app:app --host 0.0.0.0 --port 8000

echo.
echo Launching Cloudflare HTTPS public tunnel on 127.0.0.1:8000 ...
echo Share the generated https://*.trycloudflare.com link with anyone!
echo.
.\cloudflared.exe tunnel --url http://127.0.0.1:8000
pause
