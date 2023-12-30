from .marsh_schema import ma
from marshmallow import fields 

class LocationField(ma.Schema):
    latitude = fields.Float() 
    longitude = fields.Float()

class ClinicSchema(ma.Schema):
    name = fields.String(required=True, unique=True)
    address = fields.String(required=True)
    location = ma.Nested(LocationField, required=True)