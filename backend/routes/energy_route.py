"""
Energy Consumption API Routes
"""

from flask import Blueprint, jsonify, request
from controllers.energy_controller import predict_energy_consumption

energy_bp = Blueprint("energy", __name__)

@energy_bp.route("/predict", methods=["POST"])
def predict_energy():
    """
    Predict energy consumption for a trip
    
    Expects JSON body with:
    {
        "distance_km": 50.0,
        "driving_style": "Normal",
        "road_type": "city",
        "weather": "sunny",
        "elevation_gain_m": 0,  // Optional
        "avg_speed": 60  // Optional
    }
    
    Valid values:
    - driving_style: "Eco", "Normal", "Aggressive"
    - road_type: "city", "highway", "rural", "coastal"
    - weather: "sunny", "clear", "light_rain", "heavy_rain", "monsoon", "cloudy"
    """
    body = request.get_json(silent=True)
    
    if not body:
        return jsonify({"error": "Request body must be valid JSON"}), 400
    
    # Extract required fields
    required_fields = ["distance_km", "driving_style", "road_type", "weather"]
    missing_fields = [field for field in required_fields if field not in body]
    
    if missing_fields:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing_fields)}",
            "required_fields": required_fields
        }), 400
    
    # Extract optional fields with defaults
    elevation_gain_m = body.get("elevation_gain_m", 0)
    avg_speed = body.get("avg_speed", 60)
    
    # Call controller
    result = predict_energy_consumption(
        distance_km=body["distance_km"],
        driving_style=body["driving_style"],
        road_type=body["road_type"],
        weather=body["weather"],
        elevation_gain_m=elevation_gain_m,
        avg_speed=avg_speed
    )
    
    if result.get("success"):
        return jsonify(result), 200
    else:
        return jsonify(result), 400
