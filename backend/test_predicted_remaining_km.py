import requests

# Test script for predicted remaining KM API
url = "http://127.0.0.1:5000/api/predicted-remaining-km/predict"
payload = {
    "battery_capacity_kWh": 60,
    "battery_start_%": 75,
    "eff_kWh_per_km": 0.17,
    "max_possible_km": 250,
    "vehicle_model": "Leaf"
}
response = requests.post(url, json=payload)
print("Predicted Remaining KM Response:")
print(response.status_code)
print(response.json())
