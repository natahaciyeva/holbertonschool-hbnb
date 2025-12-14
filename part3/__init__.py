# app/__init__.py

from flask import Flask
from app.config import DevelopmentConfig
from app.extensions import db, jwt

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.api.v1.views import api_v1
    app.register_blueprint(api_v1)

    return app

