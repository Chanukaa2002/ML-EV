# UI Folder - File Structure

## 📋 Complete File List

### Root Files
- **index.html** - Dashboard (main landing page)
- **README.md** - Complete documentation
- **start.bat** - Windows batch startup script
- **start.ps1** - PowerShell startup script

### CSS (1 file)
```
css/
└── style.css - Complete styling system with CSS variables, responsive design
```

### JavaScript (3 files)
```
js/
├── constants.js - Configuration, API endpoints, vehicle models, cities
├── api.js - API client, endpoint functions, HTTP methods
└── utils.js - Utility functions, helpers, formatting, storage
```

### Pages (5 files)
```
pages/
├── trip-planner.html - 3-step trip planning with ML integration
├── driving-style.html - Driving style prediction
├── battery-range.html - Range calculator
├── route-optimizer.html - Route optimization
└── energy-consumption.html - Energy analysis
```

### Assets
```
assets/ - (Empty, ready for images/icons if needed)
```

---

## 📊 Statistics

- **Total Files**: 12
- **HTML Pages**: 6
- **CSS Files**: 1
- **JavaScript Files**: 3
- **Documentation**: 1
- **Scripts**: 2

## 🎯 Features Implemented

### Core Functionality
✅ Dashboard with statistics and quick actions
✅ Weather integration for Sri Lankan cities
✅ Trip planning with 3-step wizard
✅ ML-powered driving style prediction
✅ Battery range calculator with multiple factors
✅ Route optimization with charging stops
✅ Energy consumption analysis
✅ localStorage for trip history
✅ Responsive design (mobile, tablet, desktop)
✅ Dark theme with modern UI

### Technical Features
✅ Vanilla JavaScript (no frameworks)
✅ RESTful API integration
✅ Async/await for API calls
✅ Form validation
✅ Error handling
✅ Loading states
✅ Success/error notifications
✅ Distance calculation (Haversine)
✅ Data persistence (localStorage)
✅ Responsive navigation sidebar

### Pages Breakdown

**1. Dashboard (index.html)**
- Stats cards (trips, energy, range, CO₂)
- Quick action buttons
- Weather widget with city selector
- Recent activity list
- Vehicle comparison table

**2. Trip Planner (trip-planner.html)**
- Step 1: Route details (cities, vehicle, battery)
- Step 2: Driving metrics (speed, acceleration, braking)
- Step 3: Results (weather, driving style, energy, recommendations)
- Save trip functionality

**3. Driving Style (driving-style.html)**
- Input form for driving metrics
- API integration with backend
- Visual results with confidence
- Energy impact analysis
- Driving style explanations

**4. Battery Range (battery-range.html)**
- Vehicle selection with specs
- Condition inputs (style, temp, terrain, climate)
- Range calculation with multipliers
- Impact breakdown
- Vehicle comparison table

**5. Route Optimizer (route-optimizer.html)**
- Start/destination selection
- Charging stop calculation
- Distance calculation
- Priority options
- Visual route display

**6. Energy Consumption (energy-consumption.html)**
- Trip parameter inputs
- Energy breakdown
- Efficiency metrics
- Cost estimation
- Efficiency tips

## 🔌 Backend Integration

### API Endpoints Connected
- `POST /api/driving/predict` - Driving style prediction
- `GET /api/driving/demo` - Demo data
- `GET /api/external/weather` - Weather data

### Data Models Used
- Vehicle Models (5 EVs with specs)
- Sri Lankan Cities (10 cities with coordinates)
- Driving Styles (Eco, Normal, Aggressive)
- Weather units (Metric, Imperial)

## 🎨 Design System

### Color Palette
- Primary: #0ea5e9 (Sky Blue)
- Success: #10b981 (Green)
- Warning: #f59e0b (Amber)
- Danger: #ef4444 (Red)
- Background: #0f172a (Dark Navy)

### Components Built
- Cards (standard, stat, info)
- Forms (inputs, selects, buttons)
- Navigation (sidebar, mobile menu)
- Alerts (success, error, warning, info)
- Loading spinners
- Progress bars
- Badges
- Tables
- Tabs
- Modals (ready to use)

## 🚀 Quick Start

### Method 1: Automated Start
```bash
# Windows
UI\start.bat

# PowerShell
UI\start.ps1
```

### Method 2: Manual Start
```bash
# Terminal 1 - Backend
cd backend
python app.py

# Terminal 2 - Frontend
cd UI
python -m http.server 8000

# Open browser to http://localhost:8000
```

### Method 3: Live Server (VS Code)
1. Install "Live Server" extension
2. Right-click index.html
3. Select "Open with Live Server"

## 📦 No Build Process Required

✅ No npm install
✅ No webpack/vite build
✅ No transpilation
✅ No bundling
✅ Just open and run!

## 🔧 Customization Points

Easy to modify:
- `js/constants.js` - Add vehicles, cities, colors
- `css/style.css` - Change theme, colors, spacing
- `index.html` - Modify dashboard layout
- Any page - Update forms, add features

## 📱 Browser Support

✅ Chrome/Edge (Chromium)
✅ Firefox
✅ Safari
✅ Opera

Requires:
- ES6+ JavaScript support
- Fetch API
- CSS Grid & Flexbox
- localStorage

## 🎓 Learning Resources

This codebase demonstrates:
- Modern vanilla JavaScript
- RESTful API integration
- Responsive CSS design
- Form handling & validation
- Async/await patterns
- localStorage usage
- DOM manipulation
- Event handling

## 📞 Support

**Backend Issues**: Check Flask server is running on port 5000
**Frontend Issues**: Check browser console for errors
**API Issues**: Verify CORS is enabled in backend
**Styling Issues**: Check CSS file path and syntax

---

**All files created and ready to use!** 🎉
