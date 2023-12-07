import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .routes import auth_blueprint
from dotenv import load_dotenv
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    
    CORS(app)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)

    jwt = JWTManager(app)
        
    # Register blueprints
    app.register_blueprint(auth_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
