# EV Route Optimizer - Start Application Script
# PowerShell version

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " EV Route Optimizer - Start Application" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.8 or higher" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Get script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$backendDir = Join-Path (Split-Path -Parent $scriptDir) "backend"

Write-Host ""
Write-Host "[1/3] Starting Backend Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$backendDir'; python app.py"
Start-Sleep -Seconds 3

Write-Host "[2/3] Starting Frontend HTTP Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$scriptDir'; python -m http.server 8000"
Start-Sleep -Seconds 2

Write-Host "[3/3] Opening Application in Browser..." -ForegroundColor Yellow
Start-Sleep -Seconds 2
Start-Process "http://localhost:8000"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host " Application Started Successfully!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Backend:  " -NoNewline
Write-Host "http://localhost:5000" -ForegroundColor Cyan
Write-Host "Frontend: " -NoNewline
Write-Host "http://localhost:8000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to close this window..." -ForegroundColor Gray
Write-Host "(The servers will continue running in separate windows)" -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
