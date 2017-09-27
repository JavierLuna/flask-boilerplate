import unittest

from app import create_app, db
from app.models.user import User
from tests.utils import APITestClient


class TestBase(unittest.TestCase):
	"""
	Tests Base endpoints
	"""

	def setUp(self):
		self.app = create_app(config_name='testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		self.db = db
		self.client = APITestClient(self.app.test_client())
		db.create_all()
		self.u = User(name='test', email='test@test.com', password='test')
		db.session.add(self.u)
		db.session.commit()
		self.client.token = self.u.generate_auth_token().decode('ascii')

	def tearDown(self):
		db.drop_all()
		self.app_context.pop()


from . import *