import json
from flask import Blueprint, jsonify, request
from apifairy import body, response, other_responses
from .schema import NotificationSchema
from .broker_routes import publishPostNot
from .db import notification
from bson import ObjectId
from datetime import datetime


bp = Blueprint('notification', __name__, url_prefix='/notifications')

notification_schema = NotificationSchema()
notifications_schema = NotificationSchema(many = True)


@bp.route('/', methods=['POST'])
@body(notification_schema)
@response(notification_schema,200)
def post_notification(data):
    """Create a notification"""
    try:
        data["created_at"] = datetime.utcnow()

        result = notification.insert_one(data)
        try:
            message_json = json.dumps(data, default=lambda x: x.isoformat() if isinstance(x, datetime) else None)
            publishPostNot(json.dumps(message_json))
        except Exception as e:
            print(e)
            return {'Broker error': e}, 501
        return data
    except Exception as e:
        
        return {'Error': e}, 501
    

@bp.route('/<notification_id>', methods=['GET'])
@response(notification_schema,200)
@other_responses({400: 'Invalid request.', 404: 'Notification not found.'})
def get_notification(notification_id):
    """Retrieve a notification by id"""
    try:
        object_id = ObjectId(notification_id)
        result = notification.find_one({'_id': object_id})
        if result:
            return result
        else:
            return {"message": "Notification not found"}, 404
    except Exception as e:
        return jsonify({'error': str(e)}), 501


@bp.route('/', methods=['GET'])
@response(notifications_schema,200)
@other_responses({400: 'Invalid request.', 404: 'Notification not found.'})
def get_notifications():
    """Retrieve notifications list"""
    limit_param = request.args.get('limit')
    try:
        if limit_param:
            limiter = int(limit_param)
            notifications = notification.find().limit(limiter)
            return notifications
        else:
            notifications = notification.find()
            return notifications

    except Exception as e:
        return jsonify({'error': str(e)}), 404


@bp.route('/<notification_id>', methods=['DELETE'])
@other_responses({400: 'Invalid request.', 404: 'Notification not found.'})
def delete_notification(notification_id):
    """Delete a notification by id"""
    object_id = ObjectId(notification_id)
    result = notification.delete_one({'_id':object_id})
    if result.deleted_count == 1:
        return {"message":"Notification deleted successfully"}
    else:
        return jsonify({'message': 'Notification not found'}), 404
