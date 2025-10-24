from flask import Blueprint, jsonify, request

from controllers.external_api_controller import get_weather_controller, WeatherAPIError


external_bp = Blueprint("external", __name__)


@external_bp.route("/weather", methods=["GET"])
def get_weather_query():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    units = request.args.get("units", "metric")

    if lat is None or lon is None:
        return jsonify({"error": "Missing required query params: lat, lon"}), 400

    try:
        lat_f = float(lat)
        lon_f = float(lon)
    except ValueError:
        return jsonify({"error": "lat and lon must be numbers"}), 400

    try:
        data = get_weather_controller(lat_f, lon_f, units)
        return jsonify(data), 200
    except WeatherAPIError as e:
        return jsonify({"error": str(e)}), 502


@external_bp.route("/weather", methods=["POST"])
def get_weather_body():
    body = request.get_json(silent=True) or {}
    lat = body.get("lat")
    lon = body.get("lon")
    units = body.get("units", "metric")

    if lat is None or lon is None:
        return jsonify({"error": "JSON body must include lat and lon"}), 400

    try:
        lat_f = float(lat)
        lon_f = float(lon)
    except (TypeError, ValueError):
        return jsonify({"error": "lat and lon must be numbers"}), 400

    try:
        data = get_weather_controller(lat_f, lon_f, units)
        return jsonify(data), 200
    except WeatherAPIError as e:
        return jsonify({"error": str(e)}), 502
