from flask import Blueprint, jsonify, request, make_response
from apifairy import body, response
from .schema import PatientSchema
from.db import users
import requests
from bson import ObjectId 


bp = Blueprint('Patient', __name__, url_prefix='/patient')

patient_collection = users['Patient']

patientSchema = PatientSchema()

AUTH_SERVICE_URL = "http://localhost:5005/auth/"

@bp.route('/', methods=['POST'])
def create_patient():
    try:
        payload = request.get_json()

        payload['type'] = 'Patient'

        errors = patientSchema.validate(payload)
        if errors:
            return jsonify({"message": "Validation error", "errors": errors}), 400


        auth_service_url = AUTH_SERVICE_URL + "/register" 
        auth_payload = {
            "username": payload["name"],
            "email": payload["email"],
            "password": payload["password"],
            "type": payload["type"]
        }

        auth_response = requests.post(auth_service_url, json=auth_payload)

        if auth_response.status_code != 201:
            print(f"Authentication service response: {auth_response.status_code}, {auth_response.text}")
            return jsonify({"message": "Patient registration failed", "details": auth_response.text}), auth_response.status_code

        if auth_response.status_code == 201:
            result = users.insert_one(payload)
            new_patient_id = result.inserted_id
            created_patient = users.find_one({'_id': new_patient_id})

            patient_data = PatientSchema().dump(created_patient)
            response = make_response(jsonify(patient_data), 201)
            return response
        else:
            print(f"Authentication service response: {auth_response.text}")
            return jsonify({"message": "Patient registration failed"}), 500

    except Exception as e:
        print(f"Exception in create_patient: {str(e)}")
        return jsonify({"message": "An error occurred", "error": str(e)}), 500


@bp.route('/<int:patient_id>', methods=['GET'])
@response(patientSchema, 200)
def get_patient(patient_id):
    patient = users.find_one({'_id': patient_id})

    if patient:
        return patient
    else:
        return jsonify({"message": f"No patient found with ID {patient_id}"}), 404


@bp.route('/', methods=['GET'])
@response(patientSchema, 200)
def get_all_patient():
    all_patinets = list(patient_collection.find({}))
    return all_patinets

@bp.route('/<email>', methods=['GET'])
def get_patient_email(email):
    schema = PatientSchema()
    patient = users.find_one({'email': email})

    if patient:
        serialized_patient = schema.dump(patient)
        return jsonify(serialized_patient), 200
    else:
        return jsonify({"message": f"No patinet found with email {email}"}), 404


@bp.route('/<int:patient_id>', methods=['PATCH'])
@response(patientSchema, 200)
@body(patientSchema, 200)
def update_patient(patient_id):
    existing_patient = users.find_one({'_id': patient_id})

    if not existing_patient:
        return jsonify({"message": f"No patient found with ID {patient_id}"}), 404

    updated_data = request.get_json()

    errors = patientSchema.validate(updated_data)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    users.update_one({'_id': patient_id}, {'$set': updated_data})

    updated_patient = users.find_one({'_id': patient_id})
    return updated_patient

@bp.route('/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    result = users.delete_one({'_id': patient_id})

    if result.deleted_count == 1:
        return jsonify({"message": f"Patient with ID {patient_id} deleted successfully"}), 200
    else:
        return jsonify({"message": f"No dentist found with ID {patient_id}"}), 404

@bp.route('/delete_all', methods=['DELETE'])
def delete_all_patients():
    result = patient_collection.delete_many({})
    return jsonify({"message": f"{result.deleted_count} patients deleted"}), 200

