from .marsh_schema import ma

class LocationField(ma.Schema):
    latitude = ma.Float()
    longitude = ma.Float()

class ClinicSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String(required=True)
    address = ma.String(required=True)
    location = ma.Nested(LocationField, required=True)