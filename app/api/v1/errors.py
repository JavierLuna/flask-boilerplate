from app.api.v1 import api_v1, auth_v1
from app.api.v1.exceptions import ValidationError
from app.api.v1.utils import json


@api_v1.errorhandler(400)
@json
def bad_request(e):
	return {'error': 'Bad request, did you include all the data correctly?'}, 400


@api_v1.errorhandler(401)
@json
def unauthorized(e):
	return {'error': 'Unauthorized, did not provide proper auth credentials'}, 401


@api_v1.errorhandler(404)
@json
def not_found(e):
	return {'error': 'Not found'}, 404


@api_v1.errorhandler(405)
@json
def not_allowed(e):
	return {'error': 'Method not allowed'}, 405


@api_v1.errorhandler(500)
@json
def internal_server_error(e):
	return {'error': 'Internal server error'}, 500


@api_v1.errorhandler(ValidationError)
@json
def validation_error(e):
	return {'error': 'Bad request, did you include all the data correctly?', 'info': e.info}, 400


@auth_v1.error_handler
@json
def auth_error():
	return {'error': 'Unauthorized, did not provide proper auth credentials'}, 401
