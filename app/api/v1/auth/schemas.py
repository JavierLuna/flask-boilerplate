from marshmallow import fields

from app import ma


class LoginUserSchema(ma.Schema):
	email = fields.Email(required=True)
	password = fields.Str(required=True)