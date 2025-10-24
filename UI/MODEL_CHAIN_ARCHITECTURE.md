# EV Route Optimizer - AI Model Chain Architecture

## Overview
The Route Optimizer now uses a **4-step AI model chain** where predictions from earlier models feed into subsequent models. This ensures that all predictions are **made by the backend ML models**, not calculated in the frontend.

---

## Architecture Flow

```
User Input (Frontend)
    ↓
1. Driving Style Prediction Model
    ↓
2. Energy Consumption Model  ← uses driving_style from step 1
    ↓
3. Battery Range Model       ← uses efficiency from step 2
    ↓
4. Optimal Path Model        ← uses driving_style + energy from steps 1 & 2
    ↓
Display Results (Frontend)
```

---

## Model Chain Details

### **Step 1: Driving Style Prediction**
**Endpoint:** `POST /api/driving/predict`

**Input Fields (13 fields):**
```json
{
  "distance_km": 50.0,
  "elevation_gain_m": 0,
  "avg_speed": 60,
  "max_speed": 80,
  "acceleration_mean": 1.2,
  "acceleration_std": 0.36,
  "braking_intensity": 1.5,
  "trip_duration_min": 60,
  "vehicle_make": "MG",
  "vehicle_model": "ZS EV",
  "road_type": "city",
  "weather": "clear",
  "time_of_day": "evening"
}
```

**Output:**
```json
{
  "success": true,
  "predicted_driving_style": "Normal",
  "confidence_score": 0.85
}
```

**Frontend Collection:**
- User enters: avg_speed, max_speed, avg_acceleration, avg_braking, idle_time, trip_duration
- Auto-calculated: distance_km (from city coordinates)
- Defaults: vehicle_make="MG", vehicle_model="ZS EV", elevation_gain_m=0, weather="clear", time_of_day="evening"

---

### **Step 2: Energy Consumption Prediction**
**Endpoint:** `POST /api/energy/predict`

**Input Fields (6 fields):**
```json
{
  "distance_km": 50.0,
  "driving_style": "Normal",       ← FROM STEP 1
  "road_type": "city",
  "weather": "sunny",
  "elevation_gain_m": 0,
  "avg_speed": 60
}
```

**Output:**
```json
{
  "success": true,
  "predicted_energy_kWh": 8.55,
  "efficiency_kWh_per_km": 0.171
}
```

**Frontend Collection:**
- User enters: road_type (city/highway/rural/coastal)
- From Step 1: driving_style
- Auto-calculated: distance_km
- Defaults: weather="sunny", elevation_gain_m=0
- From user: avg_speed

---

### **Step 3: Battery Range Prediction**
**Endpoint:** `POST /api/battery/predict`

**Input Fields (3 fields):**
```json
{
  "battery_capacity_kWh": 50.3,
  "battery_percent": 80,
  "efficiency_kWh_per_km": 0.171  ← FROM STEP 2
}
```

**Output:**
```json
{
  "success": true,
  "predicted_range_km": 235.67,
  "theoretical_range_km": 236.84,
  "available_energy_kWh": 40.24
}
```

**Frontend Collection:**
- User enters: battery_percent
- From vehicle data: battery_capacity_kWh
- From Step 2: efficiency_kWh_per_km

---

### **Step 4: Optimal Path Prediction**
**Endpoint:** `POST /api/optimal-path/predict`

**Input Fields (8 fields):**
```json
{
  "distance_km": 50.0,
  "road_type": "city",
  "traffic_level": "medium",
  "weather": "sunny",
  "driving_style": "Normal",           ← FROM STEP 1
  "predicted_energy_kWh": 8.55,        ← FROM STEP 2
  "predicted_range_km": 235.67,        ← FROM STEP 3 (optional)
  "battery_remaining_percent": 80
}
```

**Output:**
```json
{
  "success": true,
  "predicted_travel_time_hours": 1.2,
  "input_features": {...}
}
```

**Frontend Collection:**
- User enters: traffic_level (low/medium/high)
- From user: road_type, battery_percent
- From Step 1: driving_style
- From Step 2: predicted_energy_kWh
- Defaults: weather="sunny"

---

## Frontend User Input Requirements

### **Required User Inputs:**
1. **Trip Details:**
   - Start City (dropdown)
   - End City (dropdown)
   - Vehicle (dropdown)
   - Current Battery % (number: 0-100)
   - Road Type (dropdown: city/highway/rural/coastal)
   - Traffic Level (dropdown: low/medium/high)

2. **Driving Metrics:**
   - Average Speed (km/h)
   - Max Speed (km/h)
   - Average Acceleration (m/s²)
   - Average Braking (m/s²)
   - Idle Time (%)
   - Trip Duration (minutes)

### **Auto-Calculated:**
- Distance (from city coordinates using Haversine formula)
- Vehicle specifications (from vehicle selection)

### **Default Values:**
- elevation_gain_m: 0
- weather: "sunny" or "clear"
- time_of_day: "evening"
- vehicle_make: "MG"
- vehicle_model: "ZS EV"

---

## Data Flow Example

**User Input:**
- Colombo → Kandy
- MG ZS EV
- Battery: 80%
- Road: highway
- Traffic: medium
- Avg Speed: 60 km/h
- Max Speed: 80 km/h
- Avg Accel: 1.2 m/s²
- Avg Brake: 1.5 m/s²
- Idle Time: 15%
- Duration: 120 min

**Processing:**
1. Calculate distance: ~115 km
2. Predict driving style → "Normal" (85% confidence)
3. Predict energy → 19.67 kWh (0.171 kWh/km efficiency)
4. Predict range → 235.67 km available
5. Predict optimal path → 1.9 hours travel time

**Result:**
- Can complete trip: YES ✓
- Energy needed: 19.67 kWh
- Energy available: 40.24 kWh
- Remaining battery at destination: ~41%
- Estimated travel time: 1.9 hours

---

## Backend API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/driving/predict` | POST | Predict driving style from trip metrics |
| `/api/energy/predict` | POST | Predict energy consumption |
| `/api/battery/predict` | POST | Predict remaining range |
| `/api/optimal-path/predict` | POST | Predict optimal travel time |
| `/api/external/weather` | GET | Get weather data (optional) |

---

## Key Features

✅ **All predictions made by backend ML models**
✅ **No frontend calculations** (except distance from coordinates)
✅ **Sequential model chaining** - each model uses outputs from previous models
✅ **Proper data validation** at each step
✅ **Comprehensive error handling**
✅ **Real-time status updates** during processing
✅ **Detailed AI prediction breakdown** in results

---

## Files Modified/Created

### Backend:
- ✅ `controllers/energy_controller.py` (NEW)
- ✅ `controllers/battery_range_controller.py` (NEW)
- ✅ `routes/energy_route.py` (NEW)
- ✅ `routes/battery_route.py` (NEW)
- ✅ `app.py` (updated - registered new routes)

### Frontend:
- ✅ `pages/route-optimizer.html` (completely rewritten)
- ✅ `js/constants.js` (updated API endpoints)
- ✅ `js/api.js` (updated API methods)

---

## Testing the System

1. **Start Backend:**
   ```bash
   cd backend
   python app.py
   ```

2. **Open Frontend:**
   - Open `UI/pages/route-optimizer.html` in browser
   - Or use Live Server extension

3. **Test Flow:**
   - Select start/end cities
   - Choose vehicle
   - Enter battery %
   - Select road type & traffic
   - Enter driving metrics
   - Click "Optimize Route with AI"
   - Watch sequential model predictions
   - Review comprehensive results

---

## Success Indicators

✅ All 4 model predictions complete successfully
✅ Driving style appears in results
✅ Energy consumption calculated by model
✅ Battery range predicted by model
✅ Optimal path time estimated by model
✅ Can/cannot complete trip decision shown
✅ No frontend calculations used for ML predictions
