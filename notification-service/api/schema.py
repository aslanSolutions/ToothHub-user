from marshmallow import fields
from .marsh_schema import ma

class NotificationSchema(ma.Schema):
    _id = ma.String(attribute='_id', dump_only=True)
    subject = ma.String(required=True)
    description = ma.String(required=True)
    receiver = fields.List(fields.String(), required=True)
    created_at = fields.DateTime(dump_only=True)