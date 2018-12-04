# /app.py


### IMPORTS ###
import os
from flask import Flask, jsonify, request, json, Response

from config import app_config
from model import Transaction, Investment, db

# app = Flask(__name__)
# api = Api(app)


def create_app(env_name):
    """Create app"""

    # app initialization
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    # db.init_app(app)

    @app.route("/", methods=["GET"])
    def index():
        """First endpoint"""

        return jsonify({"show": "I'm showing"})

    return app

if __name__ == "__main__":

    env_name = os.getenv("FLASK_ENV")
    app = create_app(env_name)
    # run app
    app.run(debug=True, host="0.0.0.0")
