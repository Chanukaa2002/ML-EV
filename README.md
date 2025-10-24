# 🚗⚡ EV Route Optimizer - Complete System

A comprehensive Electric Vehicle trip planning and optimization system powered by Machine Learning. This application helps EV drivers in Sri Lanka plan efficient trips with AI-powered predictions for driving style, energy consumption, battery range, and optimal routes.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Frontend Setup](#frontend-setup)
- [Backend Setup](#backend-setup)
- [API Documentation](#api-documentation)
- [ML Models](#ml-models)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

The EV Route Optimizer is a full-stack application that combines multiple machine learning models to provide comprehensive trip planning for electric vehicle users. It analyzes various factors including driving behavior, vehicle specifications, weather conditions, and route characteristics to deliver accurate predictions and recommendations.

### Key Capabilities

1. **Complete Trip Planning** - Integrated solution combining all predictions
2. **Driving Style Analysis** - ML-based prediction (Eco/Normal/Aggressive)
3. **Battery Range Estimation** - Accurate range calculations
4. **Route Optimization** - Find most efficient routes between cities
5. **Energy Consumption Prediction** - Detailed energy usage forecasts
6. **Weather Integration** - Real-time weather data for better predictions

## ✨ Features

### 🎯 Trip Planner (All-in-One)
- **Multi-step Wizard**: Guided trip planning process
- **Integrated Predictions**: Combines all ML models in one flow
- **Real-time Weather**: Fetches current conditions for destination
- **Battery Warnings**: Alerts for low battery scenarios
- **Comprehensive Results**: Complete trip summary with all metrics

### 🏎️ Driving Style Predictor
- Predicts driving style based on trip metrics
- Analyzes acceleration, braking, and speed patterns
- Provides confidence scores
- Offers personalized recommendations
- Shows impact on energy and range

### 🔋 Battery Range Calculator
- Calculates remaining range
- Accounts for vehicle-specific efficiency
- Considers current battery level
- Provides reserve recommendations
- Displays available energy

### 🗺️ Route Optimizer
- Compares multiple routes between cities
- Shows distance, time, and energy for each route
- Identifies optimal route based on efficiency
- Displays traffic levels
- Calculates efficiency metrics (kWh/km)

### ⚡ Energy Consumption Predictor
- Estimates total energy usage
- Breaks down consumption factors
- Shows battery impact visualization
- Displays efficiency ratings
- Considers weather, terrain, and driving style

### 🌤️ Weather Integration
- Real-time weather data from OpenWeather API
- Temperature, humidity, wind speed
- Weather condition impact on range
- Automatic fetching for selected locations

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend (React)                     │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  Dashboard  │  │ Trip Planner │  │ Individual Pages │   │
│  └─────────────┘  └──────────────┘  └──────────────────┘   │
└────────────────────────────┬────────────────────────────────┘
                             │ HTTP/REST API
┌────────────────────────────▼────────────────────────────────┐
│                      Backend (Flask)                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   Routes     │  │ Controllers  │  │  ML Models (pkl) │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
│  ┌──────────────┐  ┌──────────────┐                         │
│  │  External    │  │    Data      │                         │
│  │  APIs        │  │   (CSV)      │                         │
│  └──────────────┘  └──────────────┘                         │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI library
- **Vite** - Build tool and dev server
- **React Router v6** - Routing
- **Tailwind CSS** - Styling framework
- **Axios** - HTTP client
- **Recharts** - Data visualization
- **Lucide React** - Icon library
- **Leaflet** - Maps (optional)

### Backend
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin support
- **scikit-learn** - Machine learning
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **pickle** - Model serialization

### ML Models
- **Random Forest** - Driving style classification
- **Gradient Boosting** - Range prediction
- **Linear Regression** - Energy consumption
- **Decision Trees** - Route optimization

## 📁 Project Structure

```
ML-EV/
├── frontend/                      # React frontend application
│   ├── public/                    # Static assets
│   ├── src/
│   │   ├── components/           # Reusable components
│   │   │   ├── Layout/          # Sidebar, Header, Layout
│   │   │   └── UI/              # Card, Button, Input, etc.
│   │   ├── pages/               # Page components
│   │   │   ├── Dashboard/
│   │   │   ├── TripPlanner/     # ⭐ Main integrated feature
│   │   │   ├── DrivingStyle/
│   │   │   ├── BatteryRange/
│   │   │   ├── RouteOptimizer/
│   │   │   └── EnergyConsumption/
│   │   ├── services/            # API services
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── README.md
│
├── backend/                      # Flask backend application
│   ├── routes/                  # API routes
│   │   ├── driving_route.py
│   │   └── external_route.py
│   ├── controllers/             # Business logic
│   │   ├── driving_script_controller.py
│   │   └── external_api_controller.py
│   ├── models/                  # Trained ML models (.pkl)
│   │   └── driving_style.pkl
│   ├── data/                    # Training datasets (CSV)
│   │   ├── battery_range_dataset_srilanka.csv
│   │   ├── driving_style_dataset_srilanka.csv
│   │   ├── energy_consumption_dataset_srilanka.csv
│   │   └── optimal_route_dataset_srilanka.csv
│   ├── notebooks/              # Jupyter notebooks for ML
│   ├── app.py                  # Flask application entry
│   └── requirements.txt
│
└── README.md                   # This file
```

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v18+)
- **Python** (3.8+)
- **npm** or **yarn**
- **pip** (Python package manager)

### Quick Start

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/Chanukaa2002/ML-EV.git
   cd ML-EV
   ```

2. **Set up Backend:**
   ```powershell
   cd backend
   pip install -r requirements.txt
   python app.py
   ```
   Backend runs on `http://localhost:5000`

3. **Set up Frontend:**
   ```powershell
   cd ..\frontend
   npm install
   npm run dev
   ```
   Frontend runs on `http://localhost:3000`

4. **Access Application:**
   Open browser to `http://localhost:3000`

## 💻 Frontend Setup

Detailed instructions in [`frontend/README.md`](frontend/README.md) and [`frontend/SETUP.md`](frontend/SETUP.md)

```powershell
cd frontend
npm install
npm run dev
```

### Environment Configuration

Create `frontend/.env`:
```env
VITE_API_BASE_URL=http://localhost:5000/api
```

## 🔧 Backend Setup

```powershell
cd backend
pip install -r requirements.txt
python app.py
```

### Backend Requirements

The backend needs these Python packages:
- Flask
- Flask-CORS
- scikit-learn
- pandas
- numpy
- pickle (built-in)

## 📡 API Documentation

### Driving Prediction Endpoints

#### Predict Driving Style
```http
POST /api/driving/predict
Content-Type: application/json

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

**Response:**
```json
{
  "success": true,
  "predicted_driving_style": "Normal",
  "confidence_score": 0.89,
  "input_features": {...}
}
```

### Weather Endpoints

#### Get Weather Data
```http
GET /api/external/weather?lat=6.9271&lon=79.8612&units=metric
```

**Response:**
```json
{
  "coords": {"lat": 6.9271, "lon": 79.8612},
  "location": {"city": "Colombo", "country": "LK"},
  "weather": {
    "temp": 28.5,
    "feels_like": 31.2,
    "humidity": 75,
    "condition": "Clear",
    "description": "clear sky"
  }
}
```

## 🤖 ML Models

### 1. Driving Style Classification
- **Model**: Random Forest Classifier
- **Features**: Distance, speed, acceleration, braking, vehicle, conditions
- **Output**: Eco / Normal / Aggressive
- **Accuracy**: ~95%

### 2. Battery Range Prediction
- **Model**: Gradient Boosting Regressor
- **Features**: Battery capacity, efficiency, current level
- **Output**: Remaining range in km

### 3. Energy Consumption
- **Model**: Linear Regression / Random Forest
- **Features**: Distance, vehicle, driving style, weather, terrain
- **Output**: Energy in kWh

### 4. Route Optimization
- **Model**: Decision Tree / Comparison Algorithm
- **Features**: Distance, time, traffic, energy
- **Output**: Optimal route selection

## 📊 Datasets

Located in `backend/data/`:

1. **battery_range_dataset_srilanka.csv** (50K+ records)
   - Vehicle models, battery specs, efficiency, predicted range

2. **driving_style_dataset_srilanka.csv**
   - Trip metrics, driving behavior, vehicle info, classified styles

3. **energy_consumption_dataset_srilanka.csv** (50K+ records)
   - Trip details, energy consumed, battery levels

4. **optimal_route_dataset_srilanka.csv** (3K+ records)
   - Routes between cities, distance, time, energy, optimal flag

## 🎨 Screenshots

### Dashboard
![Dashboard Overview](docs/screenshots/dashboard.png)

### Trip Planner
![Trip Planner](docs/screenshots/trip-planner.png)

### Driving Style Predictor
![Driving Style](docs/screenshots/driving-style.png)

## 🔄 Data Flow - Trip Planner

```
User Input (Route & Vehicle)
         ↓
   Trip Details Form
         ↓
    ┌────┴────┐
    │  Step 1  │ → Weather API → Fetch destination weather
    └────┬────┘
         ↓
    ┌────┴────┐
    │  Step 2  │ → ML Model → Predict driving style
    └────┬────┘
         ↓
    Calculate Energy Consumption (using efficiency × multiplier)
         ↓
    Calculate Battery Impact (start % - energy used)
         ↓
    Calculate Remaining Range (battery left / efficiency)
         ↓
    ┌────┴────┐
    │  Step 3  │ → Display comprehensive results
    └─────────┘
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Development Roadmap

- [ ] Add more EV vehicle models
- [ ] Integrate real-time traffic data
- [ ] Add charging station finder
- [ ] Implement user authentication
- [ ] Save trip history
- [ ] Mobile app (React Native)
- [ ] Offline mode support
- [ ] Voice-guided navigation

## 🐛 Known Issues

- Weather API requires internet connection
- Limited to Sri Lankan cities (expandable)
- Mock data for routes (can integrate Google Maps API)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

**NIBM HDSE ML Project Team**
- Machine Learning Implementation
- Full Stack Development
- UI/UX Design

## 🙏 Acknowledgments

- OpenWeather API for weather data
- scikit-learn for ML frameworks
- React and Flask communities
- Tailwind CSS for amazing styling
- Lucide for beautiful icons

## 📞 Support

For issues and questions:
- Create an issue in GitHub
- Check existing documentation
- Review setup guides

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐!

---

**Built with ❤️ for EV enthusiasts in Sri Lanka** 🚗⚡🇱🇰
