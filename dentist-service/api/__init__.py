from flask import Flask
from apifairy import APIFairy
from flask_marshmallow import Marshmallow
from .routes import bp
from .service_routes import service_bp
from .marsh_schema import ma
from flask_cors import CORS

apifairy = APIFairy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['APIFAIRY_TITLE'] = 'Dentist API'
    app.config['APIFAIRY_VERSION'] = '1.0'

    # Initialize APIFairy, Marshmallow, and CORS
    apifairy.init_app(app)
    ma.init_app(app)
    CORS(app, origins="http://localhost:8080")

    # Register the dentsit blueprint
    app.register_blueprint(bp)
    app.register_blueprint(service_bp)

    return app