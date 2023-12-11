from flask import jsonify
from flask_jwt_extended import get_jwt, get_jti, create_access_token, get_jwt_identity
from .user_model import AuthedUser
from .db import authed_collection

def register_user(data):
    # Validate data
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing data'}), 400

    # Check if user already exists
    if AuthedUser.find_by_email(data['email'], authed_collection):
        return jsonify({'error': 'Email already exists'}), 400

    # Create new user
    try:
        new_user = AuthedUser(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            type=data['type'],
            collection=authed_collection
        )
        new_user.save()

        # Create JWT token
        access_token = create_access_token(identity=new_user.email)
        return jsonify({'message': 'User registered successfully', 'access_token': access_token}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

# Checks if the user is legit
# Function to check if the user is legitimate
def is_user_valid():
    # Get the identity of the current user (based on the JWT token)
    current_user = get_jwt_identity()
    if current_user:
        return jsonify({"message": "Token is valid", "user": current_user}), 200
    else:
        return jsonify({"message": "Invalid token"}), 401
    

def login_user(data):
    # Validate data
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400

    # Retrieve user from database
    user_data = AuthedUser.find_by_email(data['email'], authed_collection)
    if not user_data:
        return jsonify({'error': 'Invalid email or password'}), 401

    if AuthedUser.check_password(data['password'], user_data['password_hash']):
        access_token = create_access_token(identity=data['email'], additional_claims={'type': user_data['type']})

        return jsonify({
            'access_token': access_token,
            'user': {
                'email': data['email'],
                'type': user_data['type']
            }
        }), 200

    else:
        # Password does not match
        return jsonify({'error': 'Invalid email or password'}), 401
    
    
def protected_route():
    current_user_email = get_jwt_identity()
    return jsonify(message=f'Hi, {current_user_email}! This route is protected for specific users.'), 200

revoked_tokens = set()

def logout_user():
    access_token = get_jwt()
    jti = get_jti(access_token)
    revoked_tokens.add(jti)
    return jsonify(message='Logged out successfully'), 200