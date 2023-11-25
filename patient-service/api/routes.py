from flask import Blueprint, jsonify, request
from apifairy import body, response
from .schema import PatientSchema
from.db import todos

bp = Blueprint('Patient', __name__, url_prefix='/patient')

patient_collection = todos['Patient']

patientSchema = PatientSchema()

@bp.route('/<int:patient_id>', methods=['GET'])
@response(patientSchema, 200)
def get_patient(patient_id):
    # Retrieve a dentist by ID
    patient = todos.find_one({'_id': patient_id})

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
    result = todos.insert_one(payload)
    new_patient_id = result.inserted_id

    # Return the created patinet with the generated ID
    created_patient = todos.find_one({'_id': new_patient_id})
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
    existing_patient = todos.find_one({'_id': patient_id})

    if not existing_patient:
        return jsonify({"message": f"No patient found with ID {patient_id}"}), 404

    # Get the updated data from the request payload
    updated_data = request.get_json()

    # Validate the updated data against the schema
    errors = patientSchema.validate(updated_data)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    # Update the existing patinet with the new data
    todos.update_one({'_id': patient_id}, {'$set': updated_data})

    # Return the updated patient
    updated_patient = todos.find_one({'_id': patient_id})
    return updated_patient

@bp.route('/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    # Delete a patient account by ID
    result = todos.delete_one({'_id': patient_id})

    if result.deleted_count == 1:
        return jsonify({"message": f"Patient with ID {patient_id} deleted successfully"}), 200
    else:
        return jsonify({"message": f"No dentist found with ID {patient_id}"}), 404

@bp.route('/delete_all', methods=['DELETE'])
def delete_all_patients():
    # Delete all patinets from the collection
    result = patient_collection.delete_many({})
    return jsonify({"message": f"{result.deleted_count} patients deleted"}), 200

