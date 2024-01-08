from marshmallow import fields
from .marsh_schema import ma

class NotificationSchema(ma.Schema):
    _id = ma.String(attribute='_id', dump_only=True)
    appointment_datetime = ma.DateTime(required=True)
    created_at = fields.DateTime(dump_only=True)
    dentist_email = ma.String(required=True)
    patient_email = ma.String(required=True)