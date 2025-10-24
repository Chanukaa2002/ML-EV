from flask import Blueprint, jsonify, request
from controllers.energy_consumption_controller import predict_energy_consumption_controller

energy_consumption_bp = Blueprint("energy_consumption", __name__)

@energy_consumption_bp.route("/predict", methods=["POST"])
def predict_energy_consumption():
    """Predict energy consumption from input features.
    Expects JSON body with:
    {
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
    """
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Request body must be valid JSON"}), 400
    required_fields = [
        "vehicle_model", "distance_km", "driving_style", "road_type", "weather",
        "elevation_gain_m", "avg_speed", "battery_capacity_kWh", "battery_start_%", "battery_end_%"
    ]
    missing = [f for f in required_fields if f not in body]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400
    result = predict_energy_consumption_controller(body)
    if result.get("success"):
        return jsonify(result), 200
    else:
        return jsonify(result), 400
