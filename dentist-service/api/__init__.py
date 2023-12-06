from flask import Flask
from apifairy import APIFairy
from flask_marshmallow import Marshmallow
from .routes import bp
from flask_cors import CORS

apifairy = APIFairy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['APIFAIRY_TITLE'] = 'Dentist API'
    app.config['APIFAIRY_VERSION'] = '1.0'

    CORS(app)
    
    apifairy.init_app(app)
    ma.init_app(app)

    app.register_blueprint(bp)

    return app