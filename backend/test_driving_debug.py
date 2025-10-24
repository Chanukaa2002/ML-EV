"""
Debug script to test why driving style always returns Aggressive
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from controllers.driving_script_controller import predict_driving_style_controller

# Test with default frontend values - these are what's shown in the form
test_cases = [
    {
        "name": "Default Form Values (Eco-friendly)",
        "data": {
            "distance_km": 50,
            "elevation_gain_m": 100,
            "avg_speed": 60,
            "max_speed": 80,
            "acceleration_mean": 2.0,
            "acceleration_std": 0.6,  # 30% of mean
            "braking_intensity": 2.5,
            "trip_duration_min": 60,
            "vehicle_make": "MG",
            "vehicle_model": "ZS EV",
            "road_type": "city",
            "weather": "clear",
            "time_of_day": "morning"
        }
    },
    {
        "name": "Very Eco-friendly",
        "data": {
            "distance_km": 50,
            "elevation_gain_m": 50,
            "avg_speed": 40,
            "max_speed": 50,
            "acceleration_mean": 0.5,
            "acceleration_std": 0.15,
            "braking_intensity": 0.5,
            "trip_duration_min": 75,
            "vehicle_make": "MG",
            "vehicle_model": "ZS EV",
            "road_type": "highway",
            "weather": "clear",
            "time_of_day": "morning"
        }
    },
    {
        "name": "Moderate/Normal",
        "data": {
            "distance_km": 50,
            "elevation_gain_m": 100,
            "avg_speed": 50,
            "max_speed": 70,
            "acceleration_mean": 1.5,
            "acceleration_std": 0.45,
            "braking_intensity": 1.5,
            "trip_duration_min": 60,
            "vehicle_make": "Tesla",
            "vehicle_model": "Model 3",
            "road_type": "highway",
            "weather": "sunny",
            "time_of_day": "evening"
        }
    },
    {
        "name": "Actually Aggressive",
        "data": {
            "distance_km": 50,
            "elevation_gain_m": 200,
            "avg_speed": 100,
            "max_speed": 130,
            "acceleration_mean": 4.0,
            "acceleration_std": 1.2,
            "braking_intensity": 5.0,
            "trip_duration_min": 30,
            "vehicle_make": "Tesla",
            "vehicle_model": "Model 3",
            "road_type": "highway",
            "weather": "clear",
            "time_of_day": "night"
        }
    }
]

print("=" * 80)
print("DRIVING STYLE PREDICTION DEBUG")
print("=" * 80)

for test in test_cases:
    print(f"\n{'='*80}")
    print(f"Test Case: {test['name']}")
    print(f"{'='*80}")
    print("\nInput Parameters:")
    data = test['data']
    print(f"  Distance: {data['distance_km']} km")
    print(f"  Elevation: {data['elevation_gain_m']} m")
    print(f"  Avg Speed: {data['avg_speed']} km/h")
    print(f"  Max Speed: {data['max_speed']} km/h")
    print(f"  Acceleration (mean): {data['acceleration_mean']} m/s²")
    print(f"  Acceleration (std): {data['acceleration_std']} m/s²")
    print(f"  Braking: {data['braking_intensity']} m/s²")
    print(f"  Duration: {data['trip_duration_min']} min")
    print(f"  Vehicle: {data['vehicle_make']} {data['vehicle_model']}")
    print(f"  Road: {data['road_type']}")
    print(f"  Weather: {data['weather']}")
    print(f"  Time: {data['time_of_day']}")
    
    result = predict_driving_style_controller(data)
    
    print("\nPrediction Result:")
    if result.get('success'):
        print(f"  ✓ Predicted Style: {result['predicted_driving_style']}")
        print(f"  ✓ Confidence: {result.get('confidence_score', 'N/A'):.2%}" if result.get('confidence_score') else "  ✓ Confidence: N/A")
    else:
        print(f"  ✗ Error: {result.get('error')}")

print(f"\n{'='*80}")
print("Analysis Complete!")
print(f"{'='*80}\n")
