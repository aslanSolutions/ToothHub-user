from flask import jsonify
from flask_jwt_extended import create_access_token
import bcrypt
from pymongo import MongoClient

# Setup MongoDB connection
mongodb_uri = "mongodb+srv://ali:ali@aslan.im1wsjq.mongodb.net/Authentication"  # Replace with your MongoDB URI
client = MongoClient(mongodb_uri)
db = client.Authentication
authed_collection = db.authed  # Assuming 'authed' is your collection name

class AuthedUser:
    def __init__(self, username, email, password, user_type):
        self.username = username
        self.email = email
        self.password_hash = self.set_password(password)
        self.type = user_type

    def set_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def save(self):
        user_data = {
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "type": self.type
        }
        return authed_collection.insert_one(user_data)

    @classmethod
    def find_by_email(cls, email):
        return authed_collection.find_one({"email": email})

    @staticmethod
    def check_password(password, password_hash):
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

def register_user(data):
    # Validate data
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing data'}), 400

    # Check if user already exists
    if AuthedUser.find_by_email(data['email']):
        return jsonify({'error': 'Email already exists'}), 400

    # Create new user
    try:
        new_user = AuthedUser(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            user_type=data['type']
        )
        new_user.save()

        # Create JWT token
        access_token = create_access_token(identity=new_user.email)
        return jsonify({'message': 'User registered successfully', 'access_token': access_token}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def login_user(data):
    # Validate data
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400

    # Retrieve user from database
    user_data = AuthedUser.find_by_email(data['email'])
    if not user_data:
        return jsonify({'error': 'Invalid email or password'}), 401

    # Check if the password matches
    if AuthedUser.check_password(data['password'], user_data['password_hash']):
        # Password matches, create JWT token and login successful
        access_token = create_access_token(identity=data['email'])
        return jsonify(access_token=access_token), 200
    else:
        # Password does not match
        return jsonify({'error': 'Invalid email or password'}), 401
