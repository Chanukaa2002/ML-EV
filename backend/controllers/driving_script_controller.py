import os
import pickle
import pandas as pd
import numpy as np
from typing import Dict, Any, List


# Load the model once at module import time
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "driving_style.pkl")
_model = None
_label_encoder_classes = ['Aggressive', 'Eco', 'Normal']  # From the notebook


def _get_model():
    """Lazy load the pickle model."""
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        with open(MODEL_PATH, 'rb') as f:
            _model = pickle.load(f)
    return _model


def demo_driving_controller() -> Dict[str, str]:
    """Demo controller method for driving module.

    Returns a simple JSON-serializable dict indicating the controller is wired.
    """
    return {
        "module": "driving",
        "controller": "demo",
        "status": "ok",
        "message": "Driving controller demo is live",
    }


def predict_driving_style_controller(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """Predict driving style from input features.
    
    Expected input_data keys:
    - distance_km, elevation_gain_m, avg_speed, max_speed, 
      acceleration_mean, acceleration_std, braking_intensity, trip_duration_min
    - vehicle_make, vehicle_model, road_type, weather, time_of_day
    
    Returns a dict with the predicted driving style.
    """
    try:
        model = _get_model()
        
        # Expected column names after one-hot encoding (from training)
        expected_columns = [
            'distance_km', 'elevation_gain_m', 'avg_speed', 'max_speed', 
            'acceleration_mean', 'acceleration_std', 'braking_intensity', 
            'trip_duration_min', 'vehicle_make_MG', 'vehicle_make_Nissan', 
            'vehicle_make_Tesla', 'vehicle_model_Leaf', 'vehicle_model_Model 3', 
            'vehicle_model_ZS EV', 'road_type_coastal', 'road_type_highway', 
            'road_type_rural', 'weather_heavy_rain', 'weather_light_rain', 
            'weather_monsoon', 'weather_sunny', 'time_of_day_evening', 
            'time_of_day_morning', 'time_of_day_night'
        ]
        
        # Create a DataFrame from input
        df = pd.DataFrame([input_data])
        
        # One-hot encode categorical columns
        categorical_cols = ['vehicle_make', 'vehicle_model', 'road_type', 'weather', 'time_of_day']
        df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
        
        # Ensure all expected columns exist, fill missing with 0
        for col in expected_columns:
            if col not in df_encoded.columns:
                df_encoded[col] = 0
        
        # Reorder columns to match training data
        df_encoded = df_encoded[expected_columns]
        
        # Make prediction
        prediction_encoded = model.predict(df_encoded)
        
        # Decode the prediction using label encoder classes
        predicted_style = _label_encoder_classes[prediction_encoded[0]] if prediction_encoded[0] < len(_label_encoder_classes) else "Unknown"
        
        # Get probability if available
        confidence_score = None
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(df_encoded)[0]
            confidence_score = float(max(probabilities))
        
        return {
            "success": True,
            "predicted_driving_style": predicted_style,
            "confidence_score": confidence_score,
            "input_features": input_data,
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Failed to predict driving style",
        }
