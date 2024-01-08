from flask import Flask
from apifairy import APIFairy
from flask_marshmallow import Marshmallow
from .routes import bp
from .service_routes import service_bp
from .clinic_routes import clinic_bp
from .marsh_schema import ma
from flask_cors import CORS
from .config import get_config


apifairy = APIFairy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(get_config())
    # Initialize APIFairy, Marshmallow, and CORS
    apifairy.init_app(app)
    ma.init_app(app)

    # Register the dentsit blueprint
    app.register_blueprint(bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(clinic_bp)

    return app