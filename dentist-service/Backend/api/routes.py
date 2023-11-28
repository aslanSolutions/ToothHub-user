from flask import Blueprint, jsonify, request
from apifairy import body, response
from .schema import DentistSchema
from .db import todos

bp = Blueprint('dentist', __name__, url_prefix='/dentist')

dentist_collection = todos['Dentist'] 

dentistSchema = DentistSchema()

@bp.route('/<int:dentist_id>', methods=['GET'])
@response(dentistSchema, 200)
def get_dentist(dentist_id):
    # Retrieve a dentist by ID
    dentist = todos.find_one({'_id': dentist_id})

    if dentist:
        return dentist
    else:
        return jsonify({"message": f"No dentist found with ID {dentist_id}"}), 404

@bp.route('/', methods=['POST'])
@response(dentistSchema, 201)
@body(dentistSchema, 201)
def create_dentist():
    # Create dentist account
    payload = request.get_json()

    # Validate the payload against the schema
    errors = dentistSchema.validate(payload)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    # Insert the new dentist into the MongoDB collection
    result = todos.insert_one(payload)
    new_dentist_id = result.inserted_id

    # Return the created dentist with the generated ID
    created_dentist = todos.find_one({'_id': new_dentist_id})
    return created_dentist, 201

@bp.route('/', methods=['GET'])
@response(dentistSchema, 200)
def get_all_dentist():
    # Retrieve all dentsit list
    all_dentists = list(dentist_collection.find({}))
    return all_dentists


@bp.route('/<int:dentist_id>', methods=['PATCH'])
@response(dentistSchema, 200)
@body(dentistSchema, 200)
def update_dentist(dentist_id):
    # Update a dentist by ID
    existing_dentist = todos.find_one({'_id': dentist_id})

    if not existing_dentist:
        return jsonify({"message": f"No dentist found with ID {dentist_id}"}), 404

    # Get the updated data from the request payload
    updated_data = request.get_json()

    # Validate the updated data against the schema
    errors = dentistSchema.validate(updated_data)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    # Update the existing dentist with the new data
    todos.update_one({'_id': dentist_id}, {'$set': updated_data})

    # Return the updated dentist
    updated_dentist = todos.find_one({'_id': dentist_id})
    return updated_dentist

@bp.route('/<int:dentist_id>', methods=['DELETE'])
def delete_dentist(dentist_id):
    # Delete a dentist account by ID
    result = todos.delete_one({'_id': dentist_id})

    if result.deleted_count == 1:
        return jsonify({"message": f"Dentist with ID {dentist_id} deleted successfully"}), 200
    else:
        return jsonify({"message": f"No dentist found with ID {dentist_id}"}), 404

@bp.route('/delete_all', methods=['DELETE'])
def delete_all_dentists():
    # Delete all dentists from the collection
    result = dentist_collection.delete_many({})
    return jsonify({"message": f"{result.deleted_count} dentists deleted"}), 200
    