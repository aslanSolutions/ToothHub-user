from .marsh_schema import ma
from marshmallow import fields


class ServiceSchema(ma.Schema):
    _id = ma.String(attribute='_id', dump_only=True)
    text = ma.String(required=False)