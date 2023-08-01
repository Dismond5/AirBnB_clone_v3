#!/usr/bin/python3

"""Script that starts a Flask app"""

from flask import Flask, jsonify
from flask_cors import CORS
import sys
import os

# Get the current directory of the script (api/v1)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory (project root) to the Python path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from ..models import storage
from api.v1.views import app_views
from os import getenv

"""Start Flask"""
app = Flask(__name__)

"""Register the blueprint app_views"""
app.register_blueprint(app_views)

"""Create the CORS instance to allow IPs"""
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exception):
    """Closes session"""
    storage.close()


@app.errorhandler(404)
def errorhandler(error):
    """Returns a JSON-formated status code for errors"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    API_HOST = getenv("HBNB_API_HOST", "0.0.0.0")
    API_PORT = getenv("HBNB_API_PORT", 5000)
    app.run(host=API_HOST, port=API_PORT, threaded=True)
