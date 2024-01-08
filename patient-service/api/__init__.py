from flask import Flask
from flask_cors import CORS
from apifairy import APIFairy
from flask_marshmallow import Marshmallow
from .routes import bp
from .config import get_config

apifairy = APIFairy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(get_config())
    
    # Initialize APIFairy, Marshmallow
    apifairy.init_app(app)
    ma.init_app(app)

    # Register the dentsit blueprint
    app.register_blueprint(bp)

    return app