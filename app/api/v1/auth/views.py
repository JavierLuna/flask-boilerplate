from flask import request, abort
from app.api.v1.exceptions import ValidationError
from app.api.v1.utils import json
from app.models.user import User
from .schemas import LoginUserSchema
from .. import api_v1




@api_v1.route('/auth/login', methods=['POST'])
@json
def auth_login():
	json_data = request.get_json()
	if not json_data:
		abort(400)
	schema = LoginUserSchema()
	result = schema.load(json_data)
	if result.errors:
		raise ValidationError(result.errors)
	user = User.query.filter_by(email=result.data['email']).first()
	if user is not None and user.verify_password(result.data['password']):
		return {'token': user.generate_auth_token().decode('ascii')}
	else:
		abort(401)
