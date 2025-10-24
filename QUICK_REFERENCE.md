# EV Route Optimizer - Quick Reference

## 🚀 Quick Start Commands

### Initial Setup (First Time Only)
```powershell
.\setup.ps1
```

### Start Application
```powershell
# Option 1: Start both in separate windows
.\start-all.ps1

# Option 2: Start individually
.\start-backend.ps1   # Terminal 1
.\start-frontend.ps1  # Terminal 2
```

## 📍 URLs

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:3000 | React application |
| Backend API | http://localhost:5000 | Flask REST API |
| API Health | http://localhost:5000/health | Health check |

## 🎯 Main Features & Routes

| Feature | Frontend Route | Description |
|---------|---------------|-------------|
| Dashboard | `/` | Overview and navigation |
| **Trip Planner** | `/trip-planner` | ⭐ Complete integrated solution |
| Driving Style | `/driving-style` | Predict driving pattern |
| Battery Range | `/battery-range` | Calculate remaining range |
| Route Optimizer | `/route-optimizer` | Find optimal routes |
| Energy Consumption | `/energy-consumption` | Estimate energy usage |

## 🔌 API Endpoints

### Driving Prediction
```http
POST /api/driving/predict
```
**Required Fields:**
- distance_km, elevation_gain_m, avg_speed, max_speed
- acceleration_mean, acceleration_std, braking_intensity
- trip_duration_min, vehicle_make, vehicle_model
- road_type, weather, time_of_day

### Weather Data
```http
GET /api/external/weather?lat={lat}&lon={lon}
```

## 🚗 Supported Vehicles

| Make | Model | Battery (kWh) | Efficiency (kWh/km) |
|------|-------|---------------|---------------------|
| MG | ZS EV | 50 | 0.171 |
| Tesla | Model 3 | 75 | 0.150 |
| Nissan | Leaf | 60 | 0.192 |

## 🗺️ Pre-configured Cities (Sri Lanka)

- Colombo (6.9271, 79.8612)
- Kandy (7.2906, 80.6337)
- Galle (6.0535, 80.2210)
- Jaffna (9.6615, 80.0255)
- Anuradhapura (8.3114, 80.4037)

## 📊 Driving Style Categories

| Style | Energy Impact | Range Impact | Characteristics |
|-------|--------------|--------------|-----------------|
| **Eco** | -15% | +10% | Smooth, efficient |
| **Normal** | 0% | 0% | Balanced driving |
| **Aggressive** | +25% | -20% | Hard acceleration/braking |

## 🎨 Sample Data (for testing)

### Driving Style Predictor
```json
{
  "distance_km": 45.5,
  "elevation_gain_m": 120,
  "avg_speed": 55.2,
  "max_speed": 85.0,
  "acceleration_mean": 0.6,
  "acceleration_std": 0.25,
  "braking_intensity": 0.4,
  "trip_duration_min": 50,
  "vehicle_make": "Tesla",
  "vehicle_model": "Model 3",
  "road_type": "highway",
  "weather": "clear",
  "time_of_day": "morning"
}
```

## 🛠️ Development Commands

### Frontend
```powershell
cd frontend
npm run dev      # Start dev server
npm run build    # Production build
npm run preview  # Preview build
npm run lint     # Lint code
```

### Backend
```powershell
cd backend
python app.py    # Start server
```

## 🐛 Troubleshooting

### Port Already in Use
```powershell
# Find process using port 3000
netstat -ano | findstr :3000
# Kill process
taskkill /PID <PID> /F
```

### Backend Not Connecting
1. Check backend is running on port 5000
2. Verify .env file: `VITE_API_BASE_URL=http://localhost:5000/api`
3. Check CORS is enabled in Flask

### Module Not Found
```powershell
# Frontend
cd frontend
Remove-Item -Recurse -Force node_modules
npm install

# Backend
cd backend
pip install -r requirements.txt
```

## 📁 Key Files

| File | Purpose |
|------|---------|
| `frontend/.env` | Frontend environment variables |
| `backend/app.py` | Backend entry point |
| `backend/models/driving_style.pkl` | ML model |
| `frontend/src/services/api.js` | API client |
| `frontend/src/App.jsx` | Routes configuration |

## 🎯 Testing Workflow

1. **Start servers** using `.\start-all.ps1`
2. **Open browser** to http://localhost:3000
3. **Test Trip Planner:**
   - Click "Trip Planner" in sidebar
   - Click "Fill Sample" button
   - Follow the wizard
   - View integrated results
4. **Test Individual Features:**
   - Navigate using sidebar
   - Use "Fill Sample Data" buttons
   - Verify predictions work

## 📱 Mobile Testing

```powershell
# Find your IP
ipconfig

# Access from mobile (same network)
http://<YOUR_IP>:3000
```

## 🔐 Environment Variables

### Frontend (.env)
```env
VITE_API_BASE_URL=http://localhost:5000/api
```

### Backend
Backend uses environment variables for:
- HOST (default: 0.0.0.0)
- PORT (default: 5000)
- FLASK_DEBUG (default: 1)
- OPENWEATHER_API_KEY (in code, should be env var)

## 📚 Documentation

- Main README: `/README.md`
- Frontend Setup: `/frontend/SETUP.md`
- Frontend Docs: `/frontend/README.md`
- Scripts Info: `/scripts/README.md`

## 💡 Tips

- Use "Fill Sample Data" buttons for quick testing
- Check browser console for errors
- Use React DevTools for debugging
- Monitor Network tab for API calls
- Backend logs show in terminal

## 🎨 Customization

### Change Theme Colors
Edit `frontend/tailwind.config.js`

### Add New Vehicle
1. Update backend controller with specs
2. Add to frontend dropdown options
3. Update vehicle presets in components

### Add New City
1. Get coordinates (Google Maps)
2. Add to `sriLankaCoords` in TripPlanner
3. Add to dropdown options

---

**Need help?** Check the full documentation in README.md
