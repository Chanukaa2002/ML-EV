"""
Battery Range API Routes
"""

from flask import Blueprint, jsonify, request
from controllers.battery_range_controller import predict_battery_range

battery_bp = Blueprint("battery", __name__)

@battery_bp.route("/predict", methods=["POST"])
def predict_range():
    """
    Predict battery range
    
    Expects JSON body with:
    {
        "battery_capacity_kWh": 50.3,
        "battery_percent": 80,
        "efficiency_kWh_per_km": 0.171
    }
    """
    body = request.get_json(silent=True)
    
    if not body:
        return jsonify({"error": "Request body must be valid JSON"}), 400
    
    # Extract required fields
    required_fields = ["battery_capacity_kWh", "battery_percent", "efficiency_kWh_per_km"]
    missing_fields = [field for field in required_fields if field not in body]
    
    if missing_fields:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing_fields)}",
            "required_fields": required_fields
        }), 400
    
    # Call controller
    result = predict_battery_range(
        battery_capacity_kWh=body["battery_capacity_kWh"],
        battery_percent=body["battery_percent"],
        efficiency_kWh_per_km=body["efficiency_kWh_per_km"]
    )
    
    if result.get("success"):
        return jsonify(result), 200
    else:
        return jsonify(result), 400
