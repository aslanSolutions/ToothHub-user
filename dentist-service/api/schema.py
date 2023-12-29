from .marsh_schema import ma


class DentistSchema(ma.Schema):
    name = ma.String(required = True)
    email = ma.String(required = True)
    phoneNumber = ma.String(required = True)
    password = ma.String(required = True)
    type = ma.String(required=True)
    clinic_id = ma.Integer()
