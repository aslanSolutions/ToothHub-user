from flask import Blueprint, jsonify, request
from apifairy import body, response
from .clinic_schema import ClinicSchema
from .db import clinic
from bson import ObjectId 


clinic_bp = Blueprint('clinics', __name__, url_prefix='/clinics')

clinic_schema = ClinicSchema()

@clinic_bp.route('/', methods=['POST'])
@body(clinic_schema)
@response(clinic_schema, 201)
def add_clinic(clinic_data):
    data = request.get_json()
    clinic.insert_one(clinic_data)
    return clinic_data, 201


# Get all clinics
@clinic_bp.route('/', methods=['GET'])
@response(clinic_schema, 200)
def get_clinics():
    all_clinics = list(clinic.find())
    return all_clinics

# Get single clinic by ID
@clinic_bp.route('/<string:id>', methods=['GET'])
@response(clinic_schema)
def get_clinic(id):
    single_clinic = clinic.find_one({'_id': ObjectId(id)})
    if single_clinic:
        return single_clinic
    else:
        return jsonify({"message": "Clinic not found"}), 404


@clinic_bp.route('/<string:id>', methods=['PUT'])
@body(clinic_schema)
@response(clinic_schema)
def update_clinic(id):
    data = request.get_json()
    result = clinic.update_one({'_id': ObjectId(id)}, {"$set": data})
    if result.matched_count:
        return data
    else:
        return jsonify({"message": "Clinic not found"}), 404


@clinic_bp.route('/<string:id>', methods=['DELETE'])
@response(None, 204)
def delete_clinic(id):
    result = clinic.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return '', 204
    else:
        return jsonify({"message": "Clinic not found"}), 404
