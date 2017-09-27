import datetime
import uuid

import jwt
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(64), nullable=False)
	surname = db.Column(db.String(64))
	email = db.Column(db.String(100), unique=True, index=True, nullable=False)
	password_hash = db.Column(db.Text(), nullable=False)
	created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	banned = db.Column(db.Boolean, default=False)
	banned_on = db.Column(db.DateTime)

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def generate_auth_token(self, version=None):
		token = {'id': self.id, 'entropy': str(uuid.uuid4())}
		if version:
			token['api_version'] = version
		encoded = jwt.encode(token, current_app.config['SECRET_KEY'], algorithm='HS256')
		return encoded

	@staticmethod
	def verify_auth_token(token):
		try:
			data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
		except:
			return None
		user = User.query.get(data['id'])
		return user

	def __repr__(self):
		return "<User " + self.email + " >"
