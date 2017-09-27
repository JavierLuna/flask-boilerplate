from flask import Blueprint, g
from flask_httpauth import HTTPTokenAuth

from app.models.user import User

api_v1 = Blueprint('v1', __name__)
auth_v1 = HTTPTokenAuth(scheme='Token')


@auth_v1.verify_token
def verify_token(token):
	user = User.verify_auth_token(token)
	if user:
		g.user = user
		g.token = token
		return True
	return False


from . import auth, father, son, errors
