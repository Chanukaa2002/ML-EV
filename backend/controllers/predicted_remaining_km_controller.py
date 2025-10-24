import os
import pickle
import pandas as pd
from typing import Dict, Any

# Load the model once at module import time
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "Predicted_remaining_KM_model.pkl")
_model = None

# For one-hot encoding vehicle_model, we need to know all possible models
VEHICLE_MODELS = ["Leaf", "ZS EV", "Atto 3", "Model 3"]


def _get_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        with open(MODEL_PATH, 'rb') as f:
            _model = pickle.load(f)
    return _model


def predict_remaining_km_controller(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Predict remaining KM from input features."""
    try:
        model = _get_model()
        # Required features
        features = [
            'battery_capacity_kWh', 'battery_start_%', 'eff_kWh_per_km', 'max_possible_km'
        ] + [f'vehicle_model_{m}' for m in VEHICLE_MODELS]
        # Prepare input
        data = input_data.copy()
        # One-hot encode vehicle_model
        for m in VEHICLE_MODELS:
            data[f'vehicle_model_{m}'] = 1 if data.get('vehicle_model') == m else 0
        # Fill missing features with 0
        for f in features:
            if f not in data:
                data[f] = 0
        X = pd.DataFrame([{f: data[f] for f in features}])
        pred = model.predict(X)[0]
        return {"success": True, "predicted_remaining_km": float(pred)}
    except Exception as e:
        return {"success": False, "error": str(e)}
