@echo off
setlocal

:: Usage: push.bat "Your commit message"
set "MSG=%~1"
if "%MSG%"=="" set "MSG=Update"

git add .
git commit -m "%MSG%"
git push

for /f %%i in ('git rev-parse --short HEAD') do set HASH=%%i
echo.
echo ========================================
echo  Pushed! Deployed hash: %HASH%
echo ========================================
endlocal
