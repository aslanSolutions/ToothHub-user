from flask import Blueprint, request
from .auth_controller import login_user, register_user, is_user_valid, logout_user
from flask_jwt_extended import jwt_required


auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    return register_user(data)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    return login_user(data)

@auth_blueprint.route('/validate', methods=['GET'])
@jwt_required()
def validate_user_route():
    return is_user_valid()

# Function to register the auth blueprint
def register_auth_blueprint(app):
    app.register_blueprint(auth_blueprint)


@auth_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    return jsonify(message="Protected route accessed")

@auth_blueprint.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return logout_user()