# EV Route Optimizer - Vanilla HTML/CSS/JS Frontend

A modern, fully-functional frontend application for the EV Route Optimizer backend, built with pure HTML, CSS, and JavaScript (no frameworks).

## 📁 Project Structure

```
UI/
├── index.html              # Dashboard (main page)
├── pages/                  # Application pages
│   ├── trip-planner.html          # Multi-step trip planning with ML integration
│   ├── driving-style.html         # Driving style prediction
│   ├── battery-range.html         # Range calculator
│   ├── route-optimizer.html       # Route optimization with charging stations
│   └── energy-consumption.html    # Energy analysis
├── css/
│   └── style.css          # Complete styling system
├── js/
│   ├── constants.js       # Configuration and constants
│   ├── api.js            # API client and endpoint functions
│   └── utils.js          # Utility functions
└── assets/                # Static assets (if needed)
```

## 🚀 Features

### Dashboard (index.html)
- **Statistics Overview**: Total trips, energy saved, average range, CO₂ reduction
- **Quick Actions**: Fast access to all features
- **Weather Widget**: Real-time weather for Sri Lankan cities
- **Recent Activity**: Trip history from localStorage
- **Vehicle Information**: Available EV models comparison

### Trip Planner (trip-planner.html)
- **3-Step Wizard**:
  1. Route Details: Select cities, vehicle, battery level
  2. Driving Metrics: Speed, acceleration, braking patterns
  3. Results: Comprehensive trip analysis
- **ML Integration**:
  - Weather API for destination conditions
  - Driving style prediction
  - Energy consumption calculation
- **Smart Recommendations**: Based on battery level, weather, driving style
- **Trip Saving**: Store trips to localStorage

### Driving Style Predictor (driving-style.html)
- **Input Metrics**: Speed, acceleration, braking, idle time
- **ML Prediction**: Connects to `/api/driving/predict` endpoint
- **Visual Results**: Style classification (Eco/Normal/Aggressive)
- **Energy Impact Analysis**: Shows consumption impact
- **Personalized Recommendations**: Tips to improve efficiency

### Battery Range Calculator (battery-range.html)
- **Comprehensive Inputs**:
  - Vehicle selection
  - Battery level
  - Driving style
  - Temperature
  - Terrain type
  - Climate control settings
- **Smart Calculations**: Multi-factor range estimation
- **Impact Breakdown**: Shows effect of each condition
- **Vehicle Comparison**: Table comparing all EV models

### Route Optimizer (route-optimizer.html)
- **Route Planning**: Start/destination city selection
- **Charging Stops**: Automatic calculation of required stops
- **Distance Calculation**: Haversine formula for accurate distances
- **Priority Options**: Fastest, efficient, or balanced routes
- **Visual Route Display**: Step-by-step route with charging stations

### Energy Consumption (energy-consumption.html)
- **Trip Analysis**: Distance, speed, style, climate factors
- **Energy Breakdown**: Detailed consumption analysis
- **Cost Estimation**: Based on energy consumption
- **Efficiency Metrics**: km/kWh calculation
- **Efficiency Tips**: Best practices for energy saving

## 🔗 Backend Integration

### API Endpoints Used

| Endpoint | Method | Page | Purpose |
|----------|--------|------|---------|
| `/api/driving/predict` | POST | Trip Planner, Driving Style | Predict driving style from metrics |
| `/api/driving/demo` | GET | Driving Style | Get demo data |
| `/api/external/weather` | GET | Dashboard, Trip Planner | Fetch weather by coordinates |

### Request/Response Examples

**Driving Style Prediction**
```javascript
// Request
POST /api/driving/predict
{
  "avg_speed": 60,
  "max_speed": 80,
  "avg_acceleration": 2.0,
  "avg_braking": 2.5,
  "idle_time_percent": 15
}

// Response
{
  "predicted_style": "Normal",
  "confidence": 85.5
}
```

**Weather API**
```javascript
// Request
GET /api/external/weather?lat=6.9271&lon=79.8612&units=metric

// Response
{
  "main": {
    "temp": 28.5,
    "humidity": 75
  },
  "weather": [
    {
      "description": "partly cloudy"
    }
  ],
  "wind": {
    "speed": 3.5
  }
}
```

## 🎨 Design System

### Color Palette
- **Primary**: #0ea5e9 (Sky Blue)
- **Success**: #10b981 (Green)
- **Warning**: #f59e0b (Amber)
- **Danger**: #ef4444 (Red)
- **Background**: #0f172a (Dark Blue)
- **Text**: #f1f5f9 (Light Gray)

### Typography
- **Font**: Inter (Google Fonts)
- **Headings**: 600-700 weight
- **Body**: 400-500 weight

### Components
- Cards with hover effects
- Stat cards with icons
- Responsive navigation sidebar
- Form controls with validation
- Alert notifications
- Loading spinners
- Progress bars
- Badges

## 📱 Responsive Design

- **Desktop**: Full sidebar, multi-column grids
- **Tablet** (< 1024px): Collapsible sidebar, 2-column grids
- **Mobile** (< 768px): Hidden sidebar, single column
- **Small Mobile** (< 480px): Optimized spacing

## 💾 Data Storage

### localStorage Keys
- `trips`: Array of saved trip data
- Individual feature results can be cached

### Trip Data Structure
```javascript
{
  route: "Colombo → Kandy",
  distance: "115.5",
  energy: "19.65",
  energySaved: 2.95,
  range: 115.5,
  date: "Oct 24, 2025, 2:30 PM"
}
```

## 🛠️ Setup Instructions

### 1. Backend Setup
Ensure your Flask backend is running on `http://localhost:5000`

```bash
cd backend
python app.py
```

### 2. Frontend Setup

**Option A: Using Live Server (Recommended)**
1. Install VS Code extension: "Live Server"
2. Right-click `index.html` → "Open with Live Server"
3. Application opens at `http://127.0.0.1:5500`

**Option B: Using Python HTTP Server**
```bash
cd UI
python -m http.server 8000
```
Then open `http://localhost:8000`

**Option C: Direct File Access**
Simply open `index.html` in a browser (CORS may block API calls)

### 3. Configuration
Edit `js/constants.js` to change:
```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

## 🧪 Testing

### Test Checklist

**Dashboard**
- [x] Weather widget loads for selected city
- [x] Stats update when trips are saved
- [x] Quick action buttons navigate correctly
- [x] Vehicle table populates

**Trip Planner**
- [x] Step navigation works
- [x] Distance calculates between cities
- [x] Weather API fetches data
- [x] Driving style prediction calls backend
- [x] Energy consumption calculates correctly
- [x] Results display properly
- [x] Trip saves to localStorage

**Driving Style**
- [x] Form validation works
- [x] API call to `/api/driving/predict`
- [x] Results display with correct style
- [x] Recommendations show based on style

**Battery Range**
- [x] Vehicle selection updates info
- [x] Range calculates with all factors
- [x] Impact percentages display correctly
- [x] Comparison table populates

**Route Optimizer**
- [x] Distance calculation works
- [x] Charging stops calculate correctly
- [x] Route displays visually

**Energy Consumption**
- [x] Energy calculates from inputs
- [x] Breakdown shows all factors
- [x] Efficiency metrics calculate correctly

## 🔧 Customization

### Adding New Vehicle
Edit `js/constants.js`:
```javascript
const VEHICLE_MODELS = [
  // ... existing vehicles
  {
    name: 'New EV Model',
    batteryCapacity: 70,
    consumption: 0.16,
    range: 437
  }
];
```

### Adding New City
Edit `js/constants.js`:
```javascript
const SRI_LANKAN_CITIES = [
  // ... existing cities
  { name: 'New City', lat: 7.0000, lon: 80.0000 }
];
```

### Changing Theme Colors
Edit CSS variables in `css/style.css`:
```css
:root {
  --primary: #your-color;
  --bg-primary: #your-bg-color;
  /* ... */
}
```

## 📊 Data Flow

```
User Input → Form Validation → API Call → Response Processing → UI Update → localStorage
```

**Example: Trip Planner Flow**
1. User enters route details (Step 1)
2. User enters driving metrics (Step 2)
3. Click "Calculate Trip"
4. Fetch weather data from API
5. Predict driving style from API
6. Calculate energy consumption locally
7. Display comprehensive results
8. Save to localStorage
9. Update dashboard statistics

## 🐛 Troubleshooting

### API Calls Failing
- Check backend is running: `http://localhost:5000`
- Verify CORS is enabled in Flask
- Check browser console for errors
- Ensure API_BASE_URL is correct

### Weather Not Loading
- Verify city coordinates in constants.js
- Check external weather API is accessible
- Check backend weather route is working

### Styles Not Applying
- Ensure `style.css` path is correct
- Check for CSS syntax errors
- Verify Google Fonts is loading

### Data Not Persisting
- Check browser localStorage is enabled
- Clear localStorage: `localStorage.clear()`
- Check browser console for errors

## 🔒 Security Notes

- No authentication implemented (add if needed)
- API calls use HTTP (consider HTTPS for production)
- localStorage is not encrypted
- Input validation is client-side only

## 📈 Performance

- **Page Load**: < 1s (no build step)
- **API Calls**: Async/await for non-blocking
- **Images**: Minimal (SVG icons only)
- **CSS**: Single file, no preprocessor
- **JS**: Vanilla, no framework overhead

## 🤝 Contributing

To add a new page:
1. Create HTML file in `pages/`
2. Copy sidebar navigation from existing page
3. Add page link to all navigation menus
4. Create form/UI using existing components
5. Add JavaScript for functionality
6. Connect to backend API if needed

## 📝 License

This project is part of the EV Route Optimizer application.

## 👥 Support

For backend API issues, refer to backend documentation.
For frontend issues, check browser console and network tab.

---

**Built with ❤️ using vanilla HTML, CSS, and JavaScript**
