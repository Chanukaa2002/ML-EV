from flask import Blueprint, jsonify, request

from controllers.optimal_path_controller import predict_optimal_path_controller


optimal_path_bp = Blueprint("optimal_path", __name__)


@optimal_path_bp.route("/predict", methods=["POST"])
def predict_travel_time():
    """Predict expected travel time for optimal path.
    
    Expects JSON body with:
    {
        "distance_km": 50.0,
        "traffic_level": "medium",
        "driving_style": "Normal",
        "predicted_energy_kWh": 10.0,
        "lat": 6.9271,  // Optional - for weather lookup
        "lon": 79.8612,  // Optional - for weather lookup
        "weather": "sunny"  // Optional - overrides weather API
    }
    
    Valid values:
    - traffic_level: "low", "medium", "high"
    - driving_style: "Eco", "Normal", "Aggressive"
    - weather: "sunny", "cloudy", "light_rain", "heavy_rain", "monsoon"
    """
    body = request.get_json(silent=True)
    
    if not body:
        return jsonify({"error": "Request body must be valid JSON"}), 400
    
    # Extract required fields
    required_fields = [
        "distance_km", "traffic_level", "driving_style", "predicted_energy_kWh"
    ]
    
    missing_fields = [field for field in required_fields if field not in body]
    if missing_fields:
        return jsonify({
            "error": f"Missing required fields: {', '.join(missing_fields)}",
            "required_fields": required_fields
        }), 400
    
    # Extract optional fields
    lat = body.get("lat")
    lon = body.get("lon")
    weather = body.get("weather")
    
    # Call controller
    result = predict_optimal_path_controller(
        distance_km=body["distance_km"],
        traffic_level=body["traffic_level"],
        driving_style=body["driving_style"],
        predicted_energy_kWh=body["predicted_energy_kWh"],
        lat=lat,
        lon=lon,
        weather=weather
    )
    
    if result.get("success"):
        return jsonify(result), 200
    else:
        return jsonify(result), 400
