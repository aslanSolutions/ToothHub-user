import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .routes import auth_blueprint
from dotenv import load_dotenv
from datetime import timedelta

# Global set to store revoked token identifiers (JWT ID or JTI)
revoked_tokens = set()

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    
    CORS(app)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return jti in revoked_tokens


    # Register blueprints
    app.register_blueprint(auth_blueprint)

    return app
