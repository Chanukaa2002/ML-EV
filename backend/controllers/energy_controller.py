"""
Energy Consumption Prediction Controller
Predicts energy consumption based on trip parameters
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# Load dataset
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'energy_consumption_dataset_srilanka.csv')

# Global model and encoders
_model = None
_encoders = {}
_feature_columns = None

def _load_model():
    """Load and train the energy prediction model"""
    global _model, _encoders, _feature_columns
    
    if _model is not None:
        return _model
    
    # Load dataset
    df = pd.read_csv(DATA_PATH)
    
    # Features for prediction
    feature_cols = ['distance_km', 'driving_style', 'road_type', 'weather', 
                    'elevation_gain_m', 'avg_speed']
    target_col = 'energy_consumed_kWh'
    
    # Create encoders for categorical variables
    categorical_cols = ['driving_style', 'road_type', 'weather']
    
    for col in categorical_cols:
        _encoders[col] = LabelEncoder()
        df[col + '_encoded'] = _encoders[col].fit_transform(df[col])
    
    # Prepare features
    X = df[['distance_km', 'elevation_gain_m', 'avg_speed', 
            'driving_style_encoded', 'road_type_encoded', 'weather_encoded']]
    y = df[target_col]
    
    # Train model
    _model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
    _model.fit(X, y)
    
    _feature_columns = X.columns.tolist()
    
    return _model

def predict_energy_consumption(distance_km, driving_style, road_type, weather, 
                               elevation_gain_m=0, avg_speed=60):
    """
    Predict energy consumption for a trip
    
    Args:
        distance_km: Distance in kilometers
        driving_style: "Eco", "Normal", or "Aggressive"
        road_type: "city", "highway", "rural", "coastal"
        weather: "sunny", "clear", "light_rain", "heavy_rain", "monsoon", "cloudy"
        elevation_gain_m: Elevation gain in meters (optional, default 0)
        avg_speed: Average speed in km/h (optional, default 60)
    
    Returns:
        dict: Prediction results with energy consumption in kWh
    """
    try:
        # Load model
        model = _load_model()
        
        # Normalize inputs
        driving_style = driving_style.capitalize()
        road_type = road_type.lower()
        weather = weather.lower()
        
        # Map weather variations
        weather_mapping = {
            'clear': 'sunny',
            'cloudy': 'light_rain',
            'rainy': 'light_rain',
            'rain': 'light_rain'
        }
        weather = weather_mapping.get(weather, weather)
        
        # Validate inputs
        valid_driving_styles = ['Eco', 'Normal', 'Aggressive']
        valid_road_types = ['city', 'highway', 'rural', 'coastal']
        valid_weather = ['sunny', 'light_rain', 'heavy_rain', 'monsoon']
        
        if driving_style not in valid_driving_styles:
            driving_style = 'Normal'
        
        if road_type not in valid_road_types:
            road_type = 'city'
            
        if weather not in valid_weather:
            weather = 'sunny'
        
        # Encode categorical variables
        driving_style_encoded = _encoders['driving_style'].transform([driving_style])[0]
        road_type_encoded = _encoders['road_type'].transform([road_type])[0]
        weather_encoded = _encoders['weather'].transform([weather])[0]
        
        # Create feature vector
        features = pd.DataFrame({
            'distance_km': [distance_km],
            'elevation_gain_m': [elevation_gain_m],
            'avg_speed': [avg_speed],
            'driving_style_encoded': [driving_style_encoded],
            'road_type_encoded': [road_type_encoded],
            'weather_encoded': [weather_encoded]
        })
        
        # Predict
        predicted_energy = model.predict(features)[0]
        
        # Calculate efficiency
        efficiency_kwh_per_km = predicted_energy / distance_km if distance_km > 0 else 0
        
        return {
            "success": True,
            "predicted_energy_kWh": round(predicted_energy, 2),
            "efficiency_kWh_per_km": round(efficiency_kwh_per_km, 3),
            "input_data": {
                "distance_km": distance_km,
                "driving_style": driving_style,
                "road_type": road_type,
                "weather": weather,
                "elevation_gain_m": elevation_gain_m,
                "avg_speed": avg_speed
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
