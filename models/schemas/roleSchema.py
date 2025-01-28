from marshmallow import fields
from schema import ma

class Role(ma.Schema):
    id = fields.Integer(required=True)
    role_name = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'role_name')