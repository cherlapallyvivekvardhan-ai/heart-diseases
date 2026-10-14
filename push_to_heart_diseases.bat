@echo off
title Push CardioScan AI to cherlapallyvivekvardhan-ai/heart-diseases
echo =========================================================================
echo    CardioScan AI: Pushing to cherlapallyvivekvardhan-ai/heart-diseases
echo    Student: Vivek Vardhan | Machine Learning ^& AI Capstone
echo =========================================================================
echo.

cd /d "%~dp0"
set PATH=C:\Users\VIVEK VARDHAN\AppData\Local\Programs\Git\cmd;%PATH%

echo Remote repository target:
git remote -v
echo.
echo Pushing branch 'main' to GitHub...
echo (When prompted, enter your GitHub Username and Personal Access Token)
echo.

git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo =========================================================================
    echo [SUCCESS] Your project has been successfully uploaded to:
    echo https://github.com/cherlapallyvivekvardhan-ai/heart-diseases
    echo =========================================================================
) else (
    echo.
    echo [AUTHENTICATION HELP]
    echo GitHub requires a Personal Access Token (PAT) instead of your regular password.
    echo If you do not have one:
    echo 1. Go to: https://github.com/settings/tokens/new
    echo 2. Check the 'repo' scope checkbox and generate the token.
    echo 3. Copy the token (starts with ghp_...) and paste it when prompted for password.
)

pause
