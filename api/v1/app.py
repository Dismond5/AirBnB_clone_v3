#!/usr/bin/python3
"""
creating blueprint for flask
"""
from flask import Flask, make_response, jsonify
from models import storage
from os import getenv
from flask_cors import CORS
from api.v1.views import app_views


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {'origins': ['0.0.0.0']}})


@app.teardown_appcontext
def teardown_appcontext(self):
    """ closes down current session """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Create a handler for 404 errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    hosts = getenv("HBNB_API_HOST", "0.0.0.0")
    ports = getenv ("HBNB_API_PORT", "5000")
    app.run(host=hosts, port=ports, threaded=True, debug=True)
