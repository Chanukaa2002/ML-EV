import os
import csv
from typing import List, Dict

from flask import Flask, jsonify, request
from flask_cors import CORS

from routes.driving_route import driving_bp
from routes.external_route import external_bp
from routes.optimal_path_route import optimal_path_bp
from routes.energy_consumption_route import energy_consumption_bp
from routes.predicted_remaining_km_route import predicted_remaining_km_bp


def create_app() -> Flask:
	app = Flask(__name__)
	CORS(app, resources={r"/api/*": {"origins": "*"}})


	# Register blueprints
	app.register_blueprint(driving_bp, url_prefix="/api/driving")
	app.register_blueprint(external_bp, url_prefix="/api/external")
	app.register_blueprint(optimal_path_bp, url_prefix="/api/optimal-path")
	app.register_blueprint(energy_consumption_bp, url_prefix="/api/energy-consumption")
	app.register_blueprint(predicted_remaining_km_bp, url_prefix="/api/predicted-remaining-km")

	@app.route("/")
	def root():
		return jsonify("Server is Running")

	@app.route("/health")
	def health():
		return jsonify({"status": "ok"})

	@app.route("/api/ping")
	def ping():
		return jsonify({"ping": "pong"})

	
	return app


app = create_app()


if __name__ == "__main__":
	host = os.getenv("HOST", "0.0.0.0")
	port = int(os.getenv("PORT", "5000"))
	debug = os.getenv("FLASK_DEBUG", "1") == "1"
	app.run(host=host, port=port, debug=debug)

