from flask import jsonify
from flask_jwt_extended import create_access_token
from pymongo import MongoClient
from .user_model import AuthedUser
import os
from dotenv import load_dotenv
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

def login_user(data):
    # Validate data
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400

    # Retrieve user from database
    user_data = AuthedUser.find_by_email(data['email'], authed_collection)
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
