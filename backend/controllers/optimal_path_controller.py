import os
import pickle
import pandas as pd
from typing import Dict, Any, Optional

from controllers.external_api_controller import get_weather_controller, WeatherAPIError


# Load the model once at module import time
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "Optimal_Path_finder.pkl")
_model = None


def _get_model():
    """Lazy load the pickle model."""
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        with open(MODEL_PATH, 'rb') as f:
            _model = pickle.load(f)
    return _model


# Label encoding mappings from the training data
TRAFFIC_LEVEL_MAP = {"low": 1, "medium": 2, "high": 0}
WEATHER_MAP = {"sunny": 4, "cloudy": 0, "light_rain": 2, "heavy_rain": 1, "monsoon": 3, "clear": 4}
DRIVING_STYLE_MAP = {"Eco": 1, "Normal": 2, "Aggressive": 0}
ROAD_TYPE_MAP = {"city": 0, "coastal": 1, "highway": 2, "rural": 3}


def _map_weather_to_encoded(weather_data: Dict[str, Any]) -> int:
    """Map OpenWeather API response to model categories.
    
    Model expects: Sunny, Rainy, Cloudy, etc.
    OpenWeather returns: Clear, Rain, Clouds, etc.
    """
    condition = weather_data.get("weather", {}).get("condition", "").lower()
    description = weather_data.get("weather", {}).get("description", "").lower()
    
    # Map to encoded values
    if "clear" in condition or "clear" in description:
        return WEATHER_MAP["clear"]
    elif "sunny" in condition or "sunny" in description:
        return WEATHER_MAP["sunny"]
    elif "heavy" in description and "rain" in description:
        return WEATHER_MAP["heavy_rain"]
    elif "rain" in condition or "rain" in description:
        return WEATHER_MAP["light_rain"]
    elif "cloud" in condition or "cloud" in description:
        return WEATHER_MAP["cloudy"]
    elif "monsoon" in description:
        return WEATHER_MAP["monsoon"]
    else:
        return WEATHER_MAP["sunny"]  # Default


def predict_optimal_path_controller(
    distance_km: float,
    road_type: str,
    traffic_level: str,
    driving_style: str,
    predicted_energy_kWh: float,
    predicted_range_km: float,
    battery_remaining_percent: float,
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    weather: Optional[str] = None
) -> Dict[str, Any]:
    """Predict expected travel time for optimal path.
    
    Args:
        distance_km: Distance in kilometers
        road_type: Type of road (city, highway, rural, coastal)
        traffic_level: Traffic level (low, medium, high)
        driving_style: Driving style (Eco, Normal, Aggressive)
        predicted_energy_kWh: Predicted energy consumption in kWh
        predicted_range_km: Predicted remaining range in km
        battery_remaining_percent: Battery percentage remaining
        lat: Latitude for weather lookup (optional)
        lon: Longitude for weather lookup (optional)
        weather: Weather condition (sunny, cloudy, light_rain, heavy_rain, monsoon) (optional, overrides API lookup)
    
    Returns:
        Dict with predicted travel time and metadata.
    """
    try:
        model = _get_model()
        
        # Encode categorical inputs
        traffic_encoded = TRAFFIC_LEVEL_MAP.get(traffic_level.lower(), 2)  # Default to medium
        driving_encoded = DRIVING_STYLE_MAP.get(driving_style, 2)  # Default to Normal
        road_type_encoded = ROAD_TYPE_MAP.get(road_type.lower(), 0)  # Default to city
        
        # Get weather if coordinates provided and weather not specified
        weather_info = None
        if weather is None and lat is not None and lon is not None:
            try:
                weather_data = get_weather_controller(lat, lon, units="metric")
                weather_encoded = _map_weather_to_encoded(weather_data)
                weather_info = weather_data
            except WeatherAPIError as e:
                # Fall back to default if weather API fails
                weather_encoded = WEATHER_MAP["sunny"]
                weather_info = {"error": str(e), "fallback": True}
        elif weather is not None:
            weather_encoded = WEATHER_MAP.get(weather.lower(), WEATHER_MAP["sunny"])
        elif weather is None:
            # Default weather if not provided
            weather_encoded = WEATHER_MAP["sunny"]
        
        # Create input DataFrame with exact column order expected by model
        # Based on the dataset: distance_km, traffic_level, weather, driving_style, predicted_energy_kWh
        input_data = pd.DataFrame([{
            'distance_km': distance_km,
            'road_type': road_type_encoded,
            'traffic_level': traffic_encoded,
            'weather': weather_encoded,
            'driving_style': driving_encoded,
            'predicted_energy_kWh': predicted_energy_kWh,
            'predicted_range_km': predicted_range_km,
            'battery_remaining_percent': battery_remaining_percent,
        }])
        
        # Make prediction
        predicted_time = model.predict(input_data)
        
        result = {
            "success": True,
            "predicted_travel_time_min": float(predicted_time[0]),
            "predicted_travel_time_hours": float(predicted_time[0] / 60),
            "input_parameters": {
                "distance_km": distance_km,
                "road_type": road_type,
                "traffic_level": traffic_level,
                "weather": list(WEATHER_MAP.keys())[list(WEATHER_MAP.values()).index(weather_encoded)],
                "driving_style": driving_style,
                "predicted_energy_kWh": predicted_energy_kWh,
                "predicted_range_km": predicted_range_km,
                "battery_remaining_percent": battery_remaining_percent,
            }
        }
        
        # Add weather info if available
        if weather_info:
            result["weather_info"] = weather_info
        
        return result
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to predict optimal path travel time",
        }
