@echo off
echo ================================================
echo   EV ROUTE OPTIMIZER - API TESTING
echo ================================================
echo.

cd /d "%~dp0backend"

echo Running comprehensive API tests...
echo Make sure backend server is running first!
echo.
echo ================================================
echo.

python test_api.py

echo.
echo ================================================
pause
