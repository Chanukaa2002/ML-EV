# EV Route Optimizer - Complete Testing Plan

## Backend API Endpoints Testing

### 1. Driving Style Prediction API
**Endpoint:** `POST /api/driving/predict`

**Test Request:**
```json
{
  "distance_km": 50,
  "elevation_gain_m": 0,
  "avg_speed": 60,
  "max_speed": 80,
  "acceleration_mean": 1.2,
  "acceleration_std": 0.36,
  "braking_intensity": 1.5,
  "trip_duration_min": 50,
  "vehicle_make": "MG",
  "vehicle_model": "ZS EV",
  "road_type": "city",
  "weather": "sunny",
  "time_of_day": "evening"
}
```

**Expected Response:**
```json
{
  "success": true,
  "predicted_driving_style": "Normal" | "Eco" | "Aggressive",
  "confidence_score": 0.85,
  "input_features": { ... }
}
```

---

### 2. Energy Consumption Prediction API
**Endpoint:** `POST /api/energy/predict`

**Test Request:**
```json
{
  "distance_km": 50,
  "driving_style": "Normal",
  "road_type": "city",
  "weather": "sunny",
  "elevation_gain_m": 0,
  "avg_speed": 60
}
```

**Expected Response:**
```json
{
  "success": true,
  "predicted_energy_kWh": 8.55,
  "efficiency_kWh_per_km": 0.171,
  "input_data": { ... }
}
```

---

### 3. Battery Range Prediction API
**Endpoint:** `POST /api/battery/predict`

**Test Request:**
```json
{
  "battery_capacity_kWh": 50.3,
  "battery_percent": 80,
  "efficiency_kWh_per_km": 0.171
}
```

**Expected Response:**
```json
{
  "success": true,
  "predicted_range_km": 235.5,
  "theoretical_range_km": 234.9,
  "available_energy_kWh": 40.24,
  "battery_percent": 80,
  "input_data": { ... }
}
```

---

### 4. Optimal Path Prediction API
**Endpoint:** `POST /api/optimal-path/predict`

**Test Request:**
```json
{
  "distance_km": 50,
  "road_type": "city",
  "traffic_level": "medium",
  "weather": "sunny",
  "driving_style": "Normal",
  "predicted_energy_kWh": 8.55,
  "predicted_range_km": 235.5,
  "battery_remaining_percent": 80
}
```

**Expected Response:**
```json
{
  "success": true,
  "predicted_travel_time_hours": 1.25,
  "input_data": { ... }
}
```

---

## Frontend Pages Testing

### 1. Route Optimizer (`route-optimizer.html`)
**Test Flow:**
1. Select: Colombo → Kandy
2. Vehicle: MG ZS EV
3. Battery: 80%
4. Road Type: Highway
5. Traffic: Medium
6. Enter driving metrics (use defaults)
7. Click "Optimize Route with AI"

**Expected Behavior:**
- ✅ Shows 4 sequential AI predictions with status updates
- ✅ No frontend calculations for ML predictions
- ✅ Displays comprehensive AI model results
- ✅ Shows trip feasibility (can/cannot complete)
- ✅ Displays estimated battery at destination

**API Call Chain:**
```
1. /api/driving/predict (with user metrics)
   ↓
2. /api/energy/predict (with driving style from #1)
   ↓
3. /api/battery/predict (with efficiency from #2)
   ↓
4. /api/optimal-path/predict (with all previous results)
```

---

### 2. Energy Consumption (`energy-consumption.html`)
**Test Flow:**
1. Select vehicle: MG ZS EV
2. Distance: 100 km
3. Speed: 70 km/h
4. Style: Normal
5. Climate: Normal
6. Click "Analyze Energy"

**Expected Behavior:**
- ✅ Calls `/api/energy/predict` backend API
- ✅ No frontend multiplier calculations
- ✅ Displays AI predicted energy consumption
- ✅ Shows efficiency from AI model
- ✅ Shows "🤖 AI Model Analysis" label

**API Call:**
```json
POST /api/energy/predict
{
  "distance_km": 100,
  "driving_style": "Normal",
  "road_type": "city",
  "weather": "sunny",
  "avg_speed": 70
}
```

---

### 3. Battery Range (`battery-range.html`)
**Test Flow:**
1. Select vehicle: MG ZS EV
2. Battery Level: 80%
3. Driving Style: Normal
4. Temperature: 25°C
5. Terrain: Mixed
6. Climate: Normal
7. Click "Calculate Range"

**Expected Behavior:**
- ✅ Calls `/api/energy/predict` first (to get efficiency)
- ✅ Then calls `/api/battery/predict` (with predicted efficiency)
- ✅ No frontend multiplier calculations
- ✅ Displays AI predicted range
- ✅ Shows "AI Predicted Range" label
- ✅ Shows theoretical vs predicted comparison

**API Call Chain:**
```
1. /api/energy/predict (standard 100km trip with conditions)
   ↓
2. /api/battery/predict (with efficiency from #1)
```

---

### 4. Driving Style (`driving-style.html`)
**Test Flow:**
1. Enter driving metrics
2. Click "Predict Driving Style"

**Expected Behavior:**
- ✅ Transforms input to 13 required backend fields
- ✅ Calls `/api/driving/predict`
- ✅ Displays predicted_driving_style
- ✅ Shows confidence_score

---

### 5. Trip Planner (`trip-planner.html`)
**Test Flow:**
1. Enter trip details
2. Enter driving metrics
3. Click "Calculate Trip"

**Expected Behavior:**
- ✅ Calls weather API
- ✅ Calls `/api/driving/predict`
- ✅ Uses backend driving style prediction
- ✅ No frontend driving style calculations

---

## Key Validation Points

### ✅ All Pages Must:
1. **Call Backend APIs** - No ML predictions in frontend
2. **Handle Errors** - Show user-friendly error messages
3. **Show Loading States** - Display "Processing..." during API calls
4. **Transform Data Correctly** - Match backend expected format
5. **Display AI Labels** - Make it clear predictions are from AI models

### ❌ Pages Must NOT:
1. Calculate driving style with frontend logic
2. Calculate energy with multipliers in frontend
3. Calculate range with multipliers in frontend
4. Do any ML model predictions in JavaScript
5. Use hardcoded multiplier values

---

## Testing Checklist

### Backend Testing:
- [ ] Flask server starts without errors
- [ ] All 4 API endpoints are registered
- [ ] Energy prediction endpoint works
- [ ] Battery range prediction endpoint works
- [ ] Driving style endpoint works (already tested)
- [ ] Optimal path endpoint works (already exists)

### Frontend Testing:
- [ ] Route Optimizer chains 4 models sequentially
- [ ] Energy Consumption calls backend API
- [ ] Battery Range calls 2 backend APIs
- [ ] Driving Style transforms data correctly
- [ ] Trip Planner uses backend predictions
- [ ] All pages show loading states
- [ ] All pages handle errors gracefully
- [ ] No console errors in browser
- [ ] CORS is working (no CORS errors)

### Integration Testing:
- [ ] Complete end-to-end route optimization
- [ ] Data flows correctly between models
- [ ] Results are consistent and logical
- [ ] UI updates reflect backend responses
- [ ] Network tab shows correct API calls

---

## How to Test

### Start Backend:
```powershell
cd D:\NIBM\HDSE\ML\CW\ML-EV\backend
python app.py
```

### Start Frontend:
Option 1: VS Code Live Server extension
Option 2: Python HTTP server:
```powershell
cd D:\NIBM\HDSE\ML\CW\ML-EV\UI
python -m http.server 8000
```
Then open: http://localhost:8000

### Test Each Page:
1. Open browser developer tools (F12)
2. Go to Network tab
3. Test each feature
4. Verify API calls in Network tab
5. Check Console for errors

---

## Success Criteria

✅ **Backend:** All 4 API endpoints return successful responses
✅ **Frontend:** All pages use backend APIs (no frontend ML logic)
✅ **Integration:** Complete route optimization works end-to-end
✅ **UX:** Clear loading states and error messages
✅ **Performance:** API calls complete within 2-3 seconds
