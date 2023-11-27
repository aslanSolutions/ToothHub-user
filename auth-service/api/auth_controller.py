from flask import jsonify
import bcrypt
from flask_jwt_extended import JWTManager, create_access_token


def register_user(data):
    # Validate data
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing data'}), 400

    # Check if user already exists
    if User.objects(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400

    # Hash the password
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    # Create new user
    try:
        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email']
        )
        new_user.set_password(data['password'])
        new_user.save()
        new_user.save()
        
        #create JWT token
        access_token = create_access_token(identity=new_user.email)

        return jsonify({'message': 'User registered successfully', 'access_token': access_token}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def login_user(data):
    # Validate data
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400

    # Retrieve user from database
    user = User.objects(email=data['email']).first()
    if not user:
        return jsonify({'error': 'Invalid email or password'}), 401

    # Check if the password matches
    if bcrypt.checkpw(data['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
        # Password matches, create JWT token and login successful
        access_token = create_access_token(identity=data['email'])
        return jsonify(access_token=access_token), 200
    else:
        # Password does not match
        return jsonify({'error': 'Invalid email or password'}), 401