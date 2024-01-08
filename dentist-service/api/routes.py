from flask import Blueprint, jsonify, request, make_response
from apifairy import body, response
from .schema import DentistSchema
from .db import users
import requests
from bson import ObjectId 

bp = Blueprint('dentist', __name__, url_prefix='/dentist')

dentist_collection = users['Dentist'] 

dentistSchema = DentistSchema()

AUTH_SERVICE_URL = "http://localhost:5005/auth"

@bp.route('/', methods=['POST'])
def register_dentist():
    try:
        # Create Dentist account
        payload = request.get_json()

        payload['type'] = 'Dentist'
        # Validate the payload against the schema
        errors = dentistSchema.validate(payload)
        if errors:
            return jsonify({"message": "Validation error", "errors": errors}), 400

        # Make a registration request to the authentication service
        auth_service_url = AUTH_SERVICE_URL + "/register"  # Update with the correct URL
        auth_payload = {
            "username": payload["name"],  # Use relevant dentist information
            "email": payload["email"],
            "password": payload["password"],
            "type": payload['type']
        }

        auth_response = requests.post(auth_service_url, json=auth_payload)

        if auth_response.status_code == 201:
            result = users.insert_one(payload)
            new_dentist_id = result.inserted_id
            created_dentist = users.find_one({'_id': new_dentist_id})

            dentist_data = DentistSchema().dump(created_dentist)
            response = make_response(jsonify(dentist_data), 201)
            return response
        else:
            # Handle registration failure in the authentication service
            print(f"Authentication service response: {auth_response.text}")
            return jsonify({"message": "Dentist registration failed"}), 500
    
    except Exception as e:
        print(f"Exception: {str(e)}")
        return jsonify({"message": "An error occurred"}), 500
    

@bp.route('/<email>', methods=['GET'])
def get_dentist(email):
    schema = DentistSchema()
    dentist = users.find_one({'email': email})

    if dentist:
        serialized_dentist = schema.dump(dentist)
        return jsonify(serialized_dentist), 200
    else:
        return jsonify({"message": f"No dentist found with email {email}"}), 404


@bp.route('/', methods=['POST'])
@response(dentistSchema, 201)
@body(dentistSchema, 201)
def create_dentist():
    # Create dentist account
    payload = request.get_json()

    payload['type'] = 'Dentist'

    errors = dentistSchema.validate(payload)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    result = users.insert_one(payload)
    new_dentist_id = result.inserted_id

    created_dentist = users.find_one({'_id': new_dentist_id})
    return created_dentist, 201

@bp.route('/', methods=['GET'])
@response(dentistSchema, 200)
def get_all_dentist():
    all_dentists = list(dentist_collection.find({}))
    schema = DentistSchema(many=True)
    return jsonify(schema.dump(all_dentists)), 200


@bp.route('/<int:dentist_id>', methods=['PATCH'])
@response(dentistSchema, 200)
@body(dentistSchema, 200)
def update_dentist(dentist_id):
    existing_dentist = users.find_one({'_id': dentist_id})

    if not existing_dentist:
        return jsonify({"message": f"No dentist found with ID {dentist_id}"}), 404

    updated_data = request.get_json()

    errors = dentistSchema.validate(updated_data)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    users.update_one({'_id': dentist_id}, {'$set': updated_data})

    updated_dentist = users.find_one({'_id': dentist_id})
    return updated_dentist

@bp.route('/<int:dentist_id>', methods=['DELETE'])
def delete_dentist(dentist_id):
    result = users.delete_one({'_id': dentist_id})

    if result.deleted_count == 1:
        return jsonify({"message": f"Dentist with ID {dentist_id} deleted successfully"}), 200
    else:
        return jsonify({"message": f"No dentist found with ID {dentist_id}"}), 404

@bp.route('/delete_all', methods=['DELETE'])
def delete_all_dentists():
    result = dentist_collection.delete_many({})
    return jsonify({"message": f"{result.deleted_count} dentists deleted"}), 200
    

@bp.route('/set_availability', methods=['POST'])
def set_availability():
    try:
        data_from_frontend = request.get_json()

        dentist_email = data_from_frontend.get("dentist_email")

        if not dentist_email:
            return jsonify({"message": "Dentist email not found in the payload"}), 400

        availability_payload = {
            "dentist_email": dentist_email,
            "date": data_from_frontend.get("date"),
            "time_slots": data_from_frontend.get("time_slots")
        }

        availability_service_url = "http://localhost:5004/availability/set_availability"
        availability_response = requests.post(availability_service_url, json=availability_payload)

        if availability_response.status_code == 201:
            return jsonify({"message": "Availability set successfully"}), 201
        else:
            return jsonify({"message": "Failed to set availability"}), 500
    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), 500
