import os
import csv
from typing import List, Dict

from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.driving_route import driving_bp
from routes.external_route import external_bp


def create_app() -> Flask:
	app = Flask(__name__)
	CORS(app, resources={r"/api/*": {"origins": "*"}})

	# Register blueprints
	app.register_blueprint(driving_bp, url_prefix="/api/driving")
	app.register_blueprint(external_bp, url_prefix="/api/external")

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

