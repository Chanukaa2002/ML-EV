# Quick Start Scripts

## Windows PowerShell Scripts

This directory contains convenience scripts for quickly starting the application.

### setup.ps1
Initial setup script that:
- Checks for Node.js and Python
- Installs backend dependencies
- Installs frontend dependencies
- Creates .env file

**Usage:**
```powershell
.\setup.ps1
```

### start-backend.ps1
Starts the Flask backend server

**Usage:**
```powershell
.\start-backend.ps1
```

### start-frontend.ps1
Starts the React frontend development server

**Usage:**
```powershell
.\start-frontend.ps1
```

### start-all.ps1
Starts both backend and frontend in separate PowerShell windows

**Usage:**
```powershell
.\start-all.ps1
```

## Execution Policy

If you get an error about execution policy, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Manual Start

If you prefer to start manually:

**Backend:**
```powershell
cd backend
python app.py
```

**Frontend:**
```powershell
cd frontend
npm run dev
```
