from flask import Blueprint, jsonify

from controllers.driving_script_controller import demo_driving_controller


# Blueprint for driving-related endpoints
driving_bp = Blueprint("driving", __name__)


@driving_bp.route("/demo", methods=["GET"])
def demo():
	data = demo_driving_controller()
	return jsonify(data), 200
