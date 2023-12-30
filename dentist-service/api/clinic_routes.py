from flask import Blueprint, jsonify, request
from apifairy import body, response
from .clinic_schema import ClinicSchema
from .db import clinic
from bson import ObjectId, errors
from marshmallow import ValidationError
from bson import json_util



clinic_bp = Blueprint('clinics', __name__, url_prefix='/clinics')

clinic_schema = ClinicSchema()

@clinic_bp.route('/', methods=['POST'])
@body(clinic_schema)
def add_clinic(clinic_data):
    clinic_data = request.get_json()
    try:
        clinic_data['_id'] = clinic_data['name']
        result = clinic.insert_one(clinic_data)
        clinic_data['_id'] = str(result.inserted_id)
        return jsonify({"message": "Clinic added successfully", "id": clinic_data['_id']}), 201

    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400

    except errors.DuplicateKeyError:
        return jsonify({"error": "Duplicate entry"}), 409

    except errors.OperationFailure as oe:
        return jsonify({"error": "Database operation failed", "details": str(oe)}), 500

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Get all clinics
@clinic_bp.route('/', methods=['GET'])
def get_clinics():
    """
    Get a list of all clinics.

    Returns:
        List of clinics.
    """
    all_clinics = list(clinic.find())
    # Convert MongoDB's ObjectId to string
    for clinic_item in all_clinics:
        clinic_item['_id'] = str(clinic_item['_id'])
    return jsonify(all_clinics)

# Get single clinic by ID
@clinic_bp.route('/<string:id>', methods=['GET'])
@response(clinic_schema, 200)
@response(None, 404)
def get_clinic(id):
    """
    Get a single clinic by its ID.

    Args:
        id (str): The ID of the clinic.

    Returns:
        The clinic if found, or a 404 error if not found.
    """

    single_clinic = clinic.find_one({'name': id})
    if single_clinic:
        return single_clinic
    else:
        return jsonify({"message": "Clinic not found"}), 404

@clinic_bp.route('/<string:id>', methods=['PUT'])
@body(clinic_schema)
@response(clinic_schema, 200)
@response(None, 404)
def update_clinic(id):
    """
    Update a clinic by its ID.

    Args:
        id (str): The ID of the clinic.
        data (dict): The data to update the clinic with.

    Returns:
        The updated clinic if found, or a 404 error if not found.
    """

    data = request.get_json()
    result = clinic.update_one({'name': id}, {"$set": data})
    if result.matched_count:
        return data
    else:
        return jsonify({"message": "Clinic not found"}), 404

@clinic_bp.route('/<string:id>', methods=['DELETE'])
@response(None, 204)
@response(None, 404)
def delete_clinic(id):
    """
    Delete a clinic by its ID.

    Args:
        id (str): The ID of the clinic.

    Returns:
        204 if deleted successfully, or a 404 error if not found.
    """

    result = clinic.delete_one({'name': id})
    if result.deleted_count:
        return '', 204
    else:
        return jsonify({"message": "Clinic not found"}), 404
