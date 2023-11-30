from flask import Blueprint, jsonify, request
from apifairy import body, response
from .schema import PatientSchema
from.db import users
import requests
from bson import ObjectId 


bp = Blueprint('Patient', __name__, url_prefix='/patient')

patient_collection = users['Patient']

patientSchema = PatientSchema()

AUTH_SERVICE_URL = "http://localhost:5002"

@bp.route('/register', methods=['POST'])
def register_patient():
    # Create Patient account
    payload = request.get_json()

    # Validate the payload against the schema
    errors = patientSchema.validate(payload)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    # Make a registration request to the authentication service
    auth_service_url = "http://127.0.0.1:5002/auth/register"  # Update with the correct URL
    auth_payload = {
        "username": payload["name"],  # Use relevant patient information
        "email": payload["email"],
        "password": payload["password"]
    }

    auth_response = requests.post(auth_service_url, json=auth_payload)

    if auth_response.status_code == 201:
        # If registration is successful in the authentication service,
        # proceed with the patient registration in your service.
        result = users.insert_one(payload)
        new_patient_id = result.inserted_id
        created_patient = users.find_one({'_id': new_patient_id})

        # Convert ObjectId to string before returning the response
        created_patient['_id'] = str(created_patient['_id'])

        return jsonify(created_patient), 201
    else:
        # Handle registration failure in the authentication service
        print(f"Authentication service response: {auth_response.text}")
        return jsonify({"message": "Patient registration failed"}), 500

@bp.route('/<int:patient_id>', methods=['GET'])
@response(patientSchema, 200)
def get_patient(patient_id):
    # Retrieve a dentist by ID
    patient = users.find_one({'_id': patient_id})

    if patient:
        return patient
    else:
        return jsonify({"message": f"No patient found with ID {patient_id}"}), 404

@bp.route('/', methods=['POST'])
@response(patientSchema, 201)
@body(patientSchema, 201)
def create_patient():
    # Create Patient account
    payload = request.get_json()

    # Validate the payload against the schema
    errors = patientSchema.validate(payload)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    # Insert the new patient into the MongoDB collection
    result = users.insert_one(payload)
    new_patient_id = result.inserted_id

    # Return the created patinet with the generated ID
    created_patient = users.find_one({'_id': new_patient_id})
    return created_patient, 201

@bp.route('/', methods=['GET'])
@response(patientSchema, 200)
def get_all_patient():
    # Retrieve all dentsit list
    all_patinets = list(patient_collection.find({}))
    return all_patinets


@bp.route('/<int:patient_id>', methods=['PATCH'])
@response(patientSchema, 200)
@body(patientSchema, 200)
def update_patient(patient_id):
    # Update a patient by ID
    existing_patient = users.find_one({'_id': patient_id})

    if not existing_patient:
        return jsonify({"message": f"No patient found with ID {patient_id}"}), 404

    # Get the updated data from the request payload
    updated_data = request.get_json()

    # Validate the updated data against the schema
    errors = patientSchema.validate(updated_data)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    # Update the existing patinet with the new data
    users.update_one({'_id': patient_id}, {'$set': updated_data})

    # Return the updated patient
    updated_patient = users.find_one({'_id': patient_id})
    return updated_patient

@bp.route('/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    # Delete a patient account by ID
    result = users.delete_one({'_id': patient_id})

    if result.deleted_count == 1:
        return jsonify({"message": f"Patient with ID {patient_id} deleted successfully"}), 200
    else:
        return jsonify({"message": f"No dentist found with ID {patient_id}"}), 404

@bp.route('/delete_all', methods=['DELETE'])
def delete_all_patients():
    # Delete all patinets from the collection
    result = patient_collection.delete_many({})
    return jsonify({"message": f"{result.deleted_count} patients deleted"}), 200

