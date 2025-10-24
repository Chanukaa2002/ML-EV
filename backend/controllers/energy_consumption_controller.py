import os
import pickle
import pandas as pd
from typing import Dict, Any

# Load the model once at module import time
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "energy_consumption_model.pkl")
_model = None

# Label encoding mappings (update as per your dataset)
DRIVING_STYLE_MAP = {"Eco": 0, "Normal": 1, "Aggressive": 2}
ROAD_TYPE_MAP = {"city": 0, "highway": 1, "rural": 2, "coastal": 3}
WEATHER_MAP = {"sunny": 0, "cloudy": 1, "light_rain": 2, "heavy_rain": 3, "monsoon": 4}
VEHICLE_MODEL_MAP = {"Leaf": 0, "ZS EV": 1, "Atto 3": 2, "Model 3": 3}


def _get_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        with open(MODEL_PATH, 'rb') as f:
            _model = pickle.load(f)
    return _model


def predict_energy_consumption_controller(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Predict energy consumption from input features."""
    try:
        model = _get_model()
        # Prepare input features
        features = [
            'vehicle_model', 'distance_km', 'driving_style', 'road_type', 'weather',
            'elevation_gain_m', 'avg_speed', 'battery_capacity_kWh', 'battery_start_%', 'battery_end_%'
        ]
        # Encode categorical fields
        data = input_data.copy()
        data['vehicle_model'] = VEHICLE_MODEL_MAP.get(data['vehicle_model'], 0)
        data['driving_style'] = DRIVING_STYLE_MAP.get(data['driving_style'], 1)
        data['road_type'] = ROAD_TYPE_MAP.get(data['road_type'], 0)
        data['weather'] = WEATHER_MAP.get(data['weather'], 0)
        # Create DataFrame
        X = pd.DataFrame([{f: data[f] for f in features}])
        # Predict
        pred = model.predict(X)[0]
        return {"success": True, "energy_consumed_kWh": float(pred)}
    except Exception as e:
        return {"success": False, "error": str(e)}
