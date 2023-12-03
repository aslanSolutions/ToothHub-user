from marshmallow import Schema, fields

class PatientSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phoneNumber = fields.Str(required= True)
    password = fields.Str(required= True)
    type = fields.Str(required=True)