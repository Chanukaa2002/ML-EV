"""
Test script for driving style prediction API
"""
import json

# Sample test data based on the CSV structure
sample_data = {
    "distance_km": 10.5,
    "elevation_gain_m": 50,
    "avg_speed": 45.2,
    "max_speed": 80.0,
    "acceleration_mean": 0.5,
    "acceleration_std": 0.2,
    "braking_intensity": 0.3,
    "trip_duration_min": 15,
    "vehicle_make": "MG",
    "vehicle_model": "ZS EV",
    "road_type": "city",
    "weather": "clear",
    "time_of_day": "evening"
}

# Test the controller directly
if __name__ == "__main__":
    from controllers.driving_script_controller import predict_driving_style_controller
    
    print("Testing driving style prediction...")
    print(f"\nInput data:")
    print(json.dumps(sample_data, indent=2))
    
    result = predict_driving_style_controller(sample_data)
    
    print(f"\nPrediction result:")
    print(json.dumps(result, indent=2))
