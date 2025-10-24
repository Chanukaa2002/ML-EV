from flask import Blueprint, jsonify, request
from controllers.predicted_remaining_km_controller import predict_remaining_km_controller

predicted_remaining_km_bp = Blueprint("predicted_remaining_km", __name__)

@predicted_remaining_km_bp.route("/predict", methods=["POST"])
def predict_remaining_km():
    """Predict remaining KM from input features.
    Expects JSON body with:
    {
        "battery_capacity_kWh": 60,
        "battery_start_%": 75,
        "eff_kWh_per_km": 0.17,
        "max_possible_km": 250,
        "vehicle_model": "Leaf"
    }
    """
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Request body must be valid JSON"}), 400
    required_fields = [
        "battery_capacity_kWh", "battery_start_%", "eff_kWh_per_km", "max_possible_km", "vehicle_model"
    ]
    missing = [f for f in required_fields if f not in body]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400
    result = predict_remaining_km_controller(body)
    if result.get("success"):
        return jsonify(result), 200
    else:
        return jsonify(result), 400
