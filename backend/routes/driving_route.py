from flask import Blueprint, jsonify, request

from controllers.driving_script_controller import demo_driving_controller, predict_driving_style_controller


# Blueprint for driving-related endpoints
driving_bp = Blueprint("driving", __name__)


@driving_bp.route("/demo", methods=["GET"])
def demo():
	data = demo_driving_controller()
	return jsonify(data), 200


@driving_bp.route("/predict", methods=["POST"])
def predict_driving_style():
	"""Predict driving style from input features.
	
	Expects JSON body with features:
	{
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
	"""
	body = request.get_json(silent=True)
	
	if not body:
		return jsonify({"error": "Request body must be valid JSON"}), 400
	
	result = predict_driving_style_controller(body)
	
	if result.get("success"):
		return jsonify(result), 200
	else:
		return jsonify(result), 400

