import requests

# Test script for energy consumption prediction API
url = "http://127.0.0.1:5000/api/energy-consumption/predict"
payload = {
    "vehicle_model": "Leaf",
    "distance_km": 100,
    "driving_style": "Eco",
    "road_type": "city",
    "weather": "sunny",
    "elevation_gain_m": 50,
    "avg_speed": 60,
    "battery_capacity_kWh": 75,
    "battery_start_%": 80,
    "battery_end_%": 50
}
response = requests.post(url, json=payload)
print("Energy Consumption Prediction Response:")
print(response.status_code)
print(response.json())
