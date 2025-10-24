"""
Test script for optimal path prediction API
"""
import json
import os

# Set OpenWeather API key for testing (if available)
# os.environ['OPENWEATHER_API_KEY'] = 'your_key_here'

# Test 1: Without weather API (manual weather input)
print("=" * 60)
print("TEST 1: Manual weather input (no API call)")
print("=" * 60)

test_data_1 = {
    "distance_km": 50.0,
    "road_type": "Highway",
    "traffic_level": "medium",
    "driving_style": "Normal",
    "predicted_energy_kWh": 10.0,
    "predicted_range_km": 300.0,
    "battery_remaining_percent": 75.0,
    "weather": "sunny"
}

from controllers.optimal_path_controller import predict_optimal_path_controller

print("\nInput data:")
print(json.dumps(test_data_1, indent=2))

result_1 = predict_optimal_path_controller(**test_data_1)

print("\nPrediction result:")
print(json.dumps(result_1, indent=2))

# Test 2: With coordinates (will fetch weather from API if key is set)
print("\n" + "=" * 60)
print("TEST 2: With coordinates (weather API integration)")
print("=" * 60)

test_data_2 = {
    "distance_km": 100.0,
    "road_type": "City",
    "traffic_level": "high",
    "driving_style": "Aggressive",
    "predicted_energy_kWh": 20.0,
    "predicted_range_km": 250.0,
    "battery_remaining_percent": 60.0,
    "lat": 6.9271,  # Colombo, Sri Lanka
    "lon": 79.8612
}

print("\nInput data:")
print(json.dumps(test_data_2, indent=2))

result_2 = predict_optimal_path_controller(**test_data_2)

print("\nPrediction result:")
print(json.dumps(result_2, indent=2))

# Test 3: Eco driving on rural road
print("\n" + "=" * 60)
print("TEST 3: Eco driving on rural road")
print("=" * 60)

test_data_3 = {
    "distance_km": 75.0,
    "road_type": "Rural",
    "traffic_level": "low",
    "driving_style": "Eco",
    "predicted_energy_kWh": 8.0,
    "predicted_range_km": 350.0,
    "battery_remaining_percent": 85.0,
    "weather": "sunny"
}

print("\nInput data:")
print(json.dumps(test_data_3, indent=2))

result_3 = predict_optimal_path_controller(**test_data_3)

print("\nPrediction result:")
print(json.dumps(result_3, indent=2))
