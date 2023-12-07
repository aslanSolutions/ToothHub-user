from .marsh_schema import ma
from marshmallow import fields


class ServiceSchema(ma.Schema):
    _id = ma.String(attribute='_id', dump_only=True)
    name = ma.String(required=False)
    description = ma.String(required=False)
    price = ma.Integer(required=False)
    image = fields.Raw(required=False)