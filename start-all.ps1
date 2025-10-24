# Start both Backend and Frontend

Write-Host "==================================" -ForegroundColor Cyan
Write-Host "Starting EV Route Optimizer..." -ForegroundColor Cyan
Write-Host "==================================" -ForegroundColor Cyan
Write-Host ""

# Start backend in new window
Write-Host "Starting Backend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; Write-Host 'Backend Server' -ForegroundColor Green; Write-Host 'Running on: http://localhost:5000' -ForegroundColor Cyan; python app.py"

# Wait a moment for backend to start
Start-Sleep -Seconds 2

# Start frontend in new window
Write-Host "Starting Frontend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; Write-Host 'Frontend Development Server' -ForegroundColor Green; Write-Host 'Running on: http://localhost:3000' -ForegroundColor Cyan; npm run dev"

Write-Host ""
Write-Host "✓ Both servers starting in separate windows!" -ForegroundColor Green
Write-Host ""
Write-Host "Backend: http://localhost:5000" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host ""
Write-Host "To stop servers, close the respective PowerShell windows" -ForegroundColor Yellow
