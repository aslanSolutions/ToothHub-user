from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .routes import auth_blueprint  # Replace with the actual file name

def create_app():
    app = Flask(__name__)
    
    CORS(app)
    app.config['JWT_SECRET_KEY'] = 'secret_key'
    jwt = JWTManager(app)

    
    # Register blueprints
    app.register_blueprint(auth_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
