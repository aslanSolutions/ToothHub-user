from flask import Blueprint, jsonify, request
from apifairy import body, response, other_responses
from .service_schema import ServiceSchema
from .db import services
import base64
from bson import ObjectId

service_bp = Blueprint('services', __name__, url_prefix='/services')
service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)


@service_bp.route('/', methods=['POST'])
@body(service_schema)
@response(service_schema, 200)
@other_responses({400: 'Invalid request.'})
def post_service(data):
    """Create a Service"""
    try:
        # Check if an image is included in the request
        if 'image' in request.files:
            file = request.files['image']
            # Read the file data as binary
            image_data = file.read()
            image_data_base64 = base64.b64encode(image_data).decode('utf-8')
            # Set the 'image' field in the data to the binary image data
            data['image'] = image_data_base64
        result = services.insert_one(data)
        return data
    except Exception as e:
        return {'message': f'Service was not added. Error: {str(e)}'}, 404


@service_bp.route('/', methods=['GET'])
@response(services_schema, 200)
@other_responses({400: 'Invalid request.', 404: 'Services not found.'})
def get_services():
    """Get all services"""
    try:
        # Retrieve documents from MongoDB
        service_list = services.find()

        # Convert binary image data to base64 before returning the response
        serialized_services = []
        for service in service_list:
            if 'image' in service and isinstance(service['image'], bytes):
                service['image'] = base64.b64encode(service['image']).decode('utf-8')
            serialized_services.append(service)

        return serialized_services
    except Exception as e:
        return jsonify({'error': str(e)}), 404


@service_bp.route('/<service_id>', methods=['GET'])
@response(service_schema, 200)
@other_responses({400: 'Invalid request.', 404: 'Service not found.'})
def get_service(service_id):
    """Get a single service by ID"""
    try:
        # Convert service_id to ObjectId
        service_object_id = ObjectId(service_id)

        # Retrieve a single service by its ID
        service = services.find_one({'_id': service_object_id})

        if service is None:
            return {'message': 'Service not found.'}, 404

        # Convert binary image data to base64 before returning the response
        if 'image' in service and isinstance(service['image'], bytes):
            service['image'] = base64.b64encode(service['image']).decode('utf-8')
        return service
    except Exception as e:
        return {'error': str(e)}, 404


@service_bp.route('/<service_id>', methods=['DELETE'])
@other_responses({400: 'Invalid request.', 404: 'Notification not found.'})
def delete_service(service_id):
    """Delete a service by id"""
    object_id = ObjectId(service_id)
    result = services.delete_one({'_id':object_id})
    if result.deleted_count == 1:
        return {"message":"Service deleted successfully"}
    else:
        return jsonify({'message': 'Service not found'}), 404


@service_bp.route('/<service_id>', methods=['PUT'])
@response(service_schema, 200)
@body(service_schema)
@other_responses({400: 'Invalid request.', 404: 'Service not found.'})
def update_service(data, service_id):
    """Update a service by ID"""
    try:
        # Convert service_id to ObjectId
        service_object_id = ObjectId(service_id)

        # Check if the service exists
        existing_service = services.find_one({'_id': service_object_id})
        if existing_service is None:
            return {'message': 'Service not found.'}, 404

        # Access the request payload directly
        if 'image' in request.files:
            file = request.files['image']
            # Read the file data as binary
            image_data = file.read()
            image_data_base64 = base64.b64encode(image_data).decode('utf-8')
            # Set the 'image' field in the data to the binary image data
            data['image'] = image_data_base64

        # Update the service by its ID with the updated data
        services.update_one({'_id': service_object_id}, {'$set': data})

        # Retrieve the updated service
        updated_service = services.find_one({'_id': service_object_id})

        # Convert binary image data to base64 before returning the response
        if 'image' in updated_service and isinstance(updated_service['image'], bytes):
            updated_service['image'] = base64.b64encode(updated_service['image']).decode('utf-8')

        return updated_service
    except Exception as e:
        return {'error': str(e)}, 404