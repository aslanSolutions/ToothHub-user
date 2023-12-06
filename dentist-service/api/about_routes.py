from flask import Blueprint, jsonify, request
from apifairy import body, response, other_responses
from .about_schema import AboutSchema
from .db import about
from bson import ObjectId
from datetime import datetime


bp = Blueprint('about', __name__, url_prefix='/abouts')

about_schema = AboutSchema()


@bp.route('/<about_id>', methods=['GET'])
@response(about_schema,200)
@other_responses({400: 'Invalid request.', 404: 'About not found.'})
def get_about(about_id):
    """Retrieve the about text by id"""
    try:
        object_id = ObjectId(about_id)
        result = about.find_one({'_id': object_id})
        if result:
            return result
        else:
            return {"message": "About text not found"}, 404
    except Exception as e:
        return jsonify({'error': str(e)}), 501
    

@bp.route('/<about_id>', methods=['PUT'])
@response(about_schema,200)
@other_responses({400: 'Invalid request.', 404: 'About text not found.'})
def get_about(data, about_id):
    """Retrieve a about by id"""
    try:
        object_id = ObjectId(about_id)
        result = about.update_one({'_id': object_id}, {'$set': data})
        if result:
            return result
        else:
            return {"message": "About text not found"}, 404
    except Exception as e:
        return jsonify({'error': str(e)}), 501

