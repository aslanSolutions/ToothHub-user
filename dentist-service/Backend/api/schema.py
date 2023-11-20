from marshmallow import Schema, fields

class DentistSchema(Schema):
    dentist_id = fields.Str(required = True)
    name = fields.Str(required = True)
    email = fields.Str(required = True)
    phoneNumber = fields.Str(required = True)
    password = fields.Str(required = True)
