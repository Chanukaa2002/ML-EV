@echo off
echo ========================================
echo  EV Route Optimizer - Start Application
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo [1/3] Starting Backend Server...
echo.
start cmd /k "cd /d %~dp0..\backend && python app.py"
timeout /t 3 >nul

echo [2/3] Starting Frontend HTTP Server...
echo.
start cmd /k "cd /d %~dp0 && python -m http.server 8000"
timeout /t 2 >nul

echo [3/3] Opening Application in Browser...
echo.
timeout /t 2 >nul
start http://localhost:8000

echo.
echo ========================================
echo  Application Started Successfully!
echo ========================================
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:8000
echo.
echo Press any key to close this window...
echo (The servers will continue running in separate windows)
pause >nul
