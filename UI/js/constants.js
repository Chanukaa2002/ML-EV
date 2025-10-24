// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// API Endpoints
const API_ENDPOINTS = {
    // Driving Style Prediction
    DRIVING_PREDICT: '/driving/predict',
    DRIVING_DEMO: '/driving/demo',

    // Weather API
    WEATHER_GET: '/external/weather',
    WEATHER_POST: '/external/weather',

    // Battery Range
    BATTERY_PREDICT: '/battery/predict',

    // Route Optimization
    OPTIMAL_PATH_PREDICT: '/optimal-path/predict',

    // Energy Consumption
    ENERGY_PREDICT: '/energy/predict'
};

// Vehicle Models
const VEHICLE_MODELS = [{
        name: 'MG ZS EV',
        make: 'MG',
        model: 'ZS EV',
        batteryCapacity: 50.3,
        consumption: 0.171,
        range: 263
    },
    {
        name: 'Tesla Model 3',
        make: 'Tesla',
        model: 'Model 3',
        batteryCapacity: 75,
        consumption: 0.15,
        range: 491
    },
    {
        name: 'Nissan Leaf',
        make: 'Nissan',
        model: 'Leaf',
        batteryCapacity: 60,
        consumption: 0.192,
        range: 311
    },
    {
        name: 'BMW iX3',
        make: 'BMW',
        model: 'iX3',
        batteryCapacity: 80,
        consumption: 0.178,
        range: 460
    },
    {
        name: 'Hyundai Kona Electric',
        make: 'Hyundai',
        model: 'Kona Electric',
        batteryCapacity: 64,
        consumption: 0.145,
        range: 484
    }
];

// Driving Styles
const DRIVING_STYLES = {
    ECO: 'Eco',
    NORMAL: 'Normal',
    AGGRESSIVE: 'Aggressive'
};

// Sri Lankan Cities with Coordinates
const SRI_LANKAN_CITIES = [
    { name: 'Colombo', lat: 6.9271, lon: 79.8612 },
    { name: 'Kandy', lat: 7.2906, lon: 80.6337 },
    { name: 'Galle', lat: 6.0535, lon: 80.2210 },
    { name: 'Jaffna', lat: 9.6615, lon: 80.0255 },
    { name: 'Negombo', lat: 7.2008, lon: 79.8358 },
    { name: 'Trincomalee', lat: 8.5874, lon: 81.2152 },
    { name: 'Batticaloa', lat: 7.7310, lon: 81.6747 },
    { name: 'Matara', lat: 5.9549, lon: 80.5550 },
    { name: 'Anuradhapura', lat: 8.3114, lon: 80.4037 },
    { name: 'Ratnapura', lat: 6.6828, lon: 80.4034 }
];

// Weather Units
const WEATHER_UNITS = {
    METRIC: 'metric',
    IMPERIAL: 'imperial'
};

// Chart Colors
const CHART_COLORS = {
    primary: '#0ea5e9',
    secondary: '#8b5cf6',
    success: '#10b981',
    warning: '#f59e0b',
    danger: '#ef4444',
    info: '#06b6d4',
    eco: '#10b981',
    normal: '#3b82f6',
    aggressive: '#ef4444'
};

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        API_BASE_URL,
        API_ENDPOINTS,
        VEHICLE_MODELS,
        DRIVING_STYLES,
        SRI_LANKAN_CITIES,
        WEATHER_UNITS,
        CHART_COLORS
    };
}