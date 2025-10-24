"""
Battery Range Prediction Controller
Predicts remaining range based on battery status and efficiency
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import os

# Load dataset
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'battery_range_dataset_srilanka.csv')

# Global model
_model = None

def _load_model():
    """Load and train the battery range prediction model"""
    global _model
    
    if _model is not None:
        return _model
    
    # Load dataset
    df = pd.read_csv(DATA_PATH)
    
    # Features for prediction
    feature_cols = ['battery_capacity_kWh', 'battery_start_%', 'eff_kWh_per_km']
    target_col = 'predicted_remaining_km'
    
    # Prepare features
    X = df[feature_cols]
    y = df[target_col]
    
    # Train model
    _model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
    _model.fit(X, y)
    
    return _model

def predict_battery_range(battery_capacity_kWh, battery_percent, efficiency_kWh_per_km):
    """
    Predict remaining range based on battery status
    
    Args:
        battery_capacity_kWh: Total battery capacity in kWh
        battery_percent: Current battery percentage (0-100)
        efficiency_kWh_per_km: Energy efficiency in kWh per km
    
    Returns:
        dict: Prediction results with predicted range in km
    """
    try:
        # Load model
        model = _load_model()
        
        # Validate inputs
        battery_percent = max(0, min(100, battery_percent))
        
        # Create feature vector
        features = pd.DataFrame({
            'battery_capacity_kWh': [battery_capacity_kWh],
            'battery_start_%': [battery_percent],
            'eff_kWh_per_km': [efficiency_kWh_per_km]
        })
        
        # Predict
        predicted_range = model.predict(features)[0]
        
        # Calculate additional metrics
        available_energy = (battery_percent / 100) * battery_capacity_kWh
        theoretical_range = available_energy / efficiency_kWh_per_km if efficiency_kWh_per_km > 0 else 0
        
        return {
            "success": True,
            "predicted_range_km": round(predicted_range, 2),
            "theoretical_range_km": round(theoretical_range, 2),
            "available_energy_kWh": round(available_energy, 2),
            "battery_percent": battery_percent,
            "input_data": {
                "battery_capacity_kWh": battery_capacity_kWh,
                "battery_percent": battery_percent,
                "efficiency_kWh_per_km": efficiency_kWh_per_km
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
