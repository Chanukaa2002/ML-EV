# 🚀 Quick Start Guide - EV Route Optimizer UI

## ⚡ Fastest Way to Get Started

### Step 1: Start the Application

**Windows (Double-click one of these):**
```
UI/start.bat    OR    UI/start.ps1
```

**That's it!** The scripts will:
1. ✅ Start the backend server (localhost:5000)
2. ✅ Start the frontend server (localhost:8000)  
3. ✅ Open your browser automatically

---

## 🎯 What You Get

### **6 Fully Functional Pages**

1. **Dashboard** (`index.html`)
   - View statistics (trips, energy, CO₂)
   - Check weather for Sri Lankan cities
   - Quick access to all features
   - See recent activity

2. **Trip Planner** (`pages/trip-planner.html`) ⭐ **Main Feature**
   - Plan trips between cities
   - Get weather forecasts
   - Predict driving style with ML
   - Calculate energy consumption
   - Receive smart recommendations

3. **Driving Style Predictor** (`pages/driving-style.html`)
   - Input driving metrics
   - ML prediction (Eco/Normal/Aggressive)
   - Energy impact analysis
   - Personalized tips

4. **Battery Range Calculator** (`pages/battery-range.html`)
   - Select vehicle model
   - Input conditions (temp, terrain, etc.)
   - Calculate real-world range
   - See impact of each factor

5. **Route Optimizer** (`pages/route-optimizer.html`)
   - Plan routes with charging stops
   - Calculate distances
   - Optimize for speed/efficiency

6. **Energy Consumption** (`pages/energy-consumption.html`)
   - Analyze trip energy usage
   - Get cost estimates
   - View efficiency metrics
   - Learn saving tips

---

## 📱 How to Use

### Dashboard
1. Open http://localhost:8000
2. Select a city from dropdown to see weather
3. Click any "Quick Action" button to navigate
4. Stats update as you save trips

### Trip Planner (Step-by-Step)
1. **Step 1**: Select start/end cities, vehicle, battery level
2. **Step 2**: Enter driving patterns (speed, acceleration, etc.)
3. **Step 3**: View results:
   - Weather conditions
   - Predicted driving style
   - Energy consumption
   - Battery status
   - Smart recommendations
4. Click "Save Trip" to store in history

### Driving Style Predictor
1. Enter your typical driving metrics:
   - Average speed (km/h)
   - Max speed (km/h)
   - Acceleration (m/s²)
   - Braking (m/s²)
   - Idle time (%)
2. Click "Predict Driving Style"
3. See your style classification
4. Get tips to improve efficiency

### Battery Range Calculator
1. Select your EV model
2. Set current battery level
3. Choose driving style
4. Enter temperature
5. Select terrain type
6. Set climate control
7. Click "Calculate Range"
8. See estimated range with breakdown

### Route Optimizer
1. Select start and destination
2. Choose vehicle
3. Set current battery
4. Set max charging stops
5. Choose priority (fastest/efficient/balanced)
6. Click "Optimize Route"
7. See distance, energy, and charging stops

### Energy Consumption
1. Select vehicle
2. Enter trip distance
3. Set average speed
4. Choose driving style
5. Set climate control
6. Click "Analyze Consumption"
7. View energy breakdown and efficiency

---

## 🔧 Features at a Glance

| Feature | Technology | Backend API |
|---------|-----------|-------------|
| Weather Integration | Fetch API | ✅ `/api/external/weather` |
| Driving Prediction | ML Model | ✅ `/api/driving/predict` |
| Distance Calculation | Haversine Formula | ❌ Client-side |
| Energy Calculation | Custom Logic | ❌ Client-side |
| Trip History | localStorage | ❌ Client-side |
| Responsive Design | CSS Grid/Flexbox | ❌ Pure CSS |

---

## 💡 Pro Tips

### Save Your Trips
- Trip Planner automatically saves completed trips
- View history on Dashboard "Recent Activity"
- Stats update automatically

### Best Practices
1. **Start with Trip Planner** - It's the main integrated feature
2. **Check Weather First** - Affects energy consumption
3. **Use Eco Mode** - Save 15-30% energy
4. **Plan Charging Stops** - For trips > 200km

### Keyboard Shortcuts
- `F5` - Refresh page
- `F12` - Open developer tools (check console)
- `Ctrl+Shift+I` - Open dev tools

---

## 🎨 Customization

### Change Backend URL
Edit `UI/js/constants.js`:
```javascript
const API_BASE_URL = 'http://your-server:5000/api';
```

### Add New Vehicle
Edit `UI/js/constants.js`:
```javascript
const VEHICLE_MODELS = [
  // Add your vehicle
  {
    name: 'Tesla Model Y',
    batteryCapacity: 75,
    consumption: 0.165,
    range: 450
  }
];
```

### Add New City
Edit `UI/js/constants.js`:
```javascript
const SRI_LANKAN_CITIES = [
  // Add your city
  { name: 'Nuwara Eliya', lat: 6.9497, lon: 80.7891 }
];
```

### Change Theme
Edit `UI/css/style.css`:
```css
:root {
  --primary: #your-color;
  --bg-primary: #your-background;
}
```

---

## 🐛 Troubleshooting

### Backend Not Connecting
**Problem**: API calls fail with network error
**Solution**:
1. Check backend is running: http://localhost:5000
2. Verify CORS is enabled in Flask
3. Check browser console (F12)

### Weather Not Loading
**Problem**: Weather widget shows error
**Solution**:
1. Ensure backend `/api/external/weather` is working
2. Test directly: http://localhost:5000/api/external/weather?lat=6.9271&lon=79.8612
3. Check internet connection

### Page Not Loading
**Problem**: Blank page or errors
**Solution**:
1. Check console (F12) for errors
2. Verify all files are in correct folders
3. Clear browser cache (Ctrl+Shift+Delete)

### Styles Not Applying
**Problem**: Page looks unstyled
**Solution**:
1. Check `css/style.css` exists
2. Verify file path in HTML
3. Check for CSS syntax errors

### Data Not Saving
**Problem**: Trips not persisting
**Solution**:
1. Check browser localStorage is enabled
2. Clear storage: Console → `localStorage.clear()`
3. Check for JavaScript errors

---

## 📊 Testing Checklist

Before deploying, test these scenarios:

**Dashboard**
- [ ] Page loads without errors
- [ ] Weather loads for Colombo
- [ ] Quick action buttons work
- [ ] Vehicle table displays

**Trip Planner**
- [ ] Can select different cities
- [ ] Distance calculates correctly
- [ ] Weather fetches for destination
- [ ] Driving style predicts (requires backend)
- [ ] Results display properly
- [ ] Trip saves successfully

**All Features**
- [ ] Navigation works between pages
- [ ] Forms validate correctly
- [ ] Error messages display
- [ ] Success messages show
- [ ] Mobile responsive works

---

## 🎓 Learning Path

**New to this project?** Follow this order:

1. **Start Here**: Open Dashboard (index.html)
2. **Explore**: Try Trip Planner with sample data
3. **Experiment**: Test Driving Style Predictor
4. **Learn**: Check Battery Range Calculator
5. **Advanced**: Use Route Optimizer
6. **Analyze**: Review Energy Consumption

---

## 📞 Need Help?

### Check These First
1. Browser Console (F12) - Shows JavaScript errors
2. Network Tab (F12) - Shows API calls
3. Backend Terminal - Shows server logs
4. README.md - Full documentation

### Common Issues
- **CORS Error**: Backend CORS not configured
- **404 Error**: Check file paths
- **API Error**: Backend not running
- **Blank Results**: Missing data in form

---

## 🎯 Next Steps

### Enhance Your App
1. Add more Sri Lankan cities
2. Include more EV models
3. Customize color theme
4. Add charging station locations
5. Implement user authentication
6. Add trip export (CSV/PDF)
7. Create charts with Chart.js
8. Add map visualization

### Deploy to Production
1. Set up proper backend server
2. Use HTTPS for security
3. Optimize images and assets
4. Enable caching
5. Add error tracking
6. Set up monitoring

---

**Enjoy using your EV Route Optimizer!** 🚗⚡

Need more help? Check:
- `README.md` - Complete documentation
- `FILE_STRUCTURE.md` - File organization
- Backend documentation - API details
