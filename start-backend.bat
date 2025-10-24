@echo off
echo ================================================
echo   EV ROUTE OPTIMIZER - BACKEND SERVER
echo ================================================
echo.

cd /d "%~dp0backend"

echo Starting Flask backend on http://localhost:5000
echo.
echo Press CTRL+C to stop the server
echo ================================================
echo.

python app.py

pause
