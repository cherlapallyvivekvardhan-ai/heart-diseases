@echo off
title Push CardioScan AI to GitHub
echo =========================================================================
echo    CardioScan AI: Push to GitHub Repository
echo    Student: Vivek Vardhan | Machine Learning ^& AI Capstone
echo =========================================================================
echo.

cd /d "%~dp0"
set PATH=C:\Users\VIVEK VARDHAN\AppData\Local\Programs\Git\cmd;%PATH%

echo Your local repository is committed and ready on branch 'main'.
echo.
echo Please create a new empty repository on GitHub (https://github.com/new).
echo Do NOT initialize it with README, .gitignore, or license.
echo.
set /p REPO_URL="Enter your GitHub Repository URL (e.g. https://github.com/username/heart-disease-capstone.git): "

if "%REPO_URL%"=="" (
    echo Error: No repository URL provided.
    pause
    exit /b
)

echo.
echo Setting remote origin to %REPO_URL% ...
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main

echo.
echo Pushing to GitHub...
echo (If prompted for credentials, use your GitHub username and Personal Access Token)
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo =========================================================================
    echo [SUCCESS] Your project has been successfully pushed to GitHub!
    echo =========================================================================
) else (
    echo.
    echo [NOTE] If authentication failed, generate a GitHub Personal Access Token at:
    echo        https://github.com/settings/tokens (with 'repo' scope)
    echo        and use it as your password when git prompts you.
)

pause
