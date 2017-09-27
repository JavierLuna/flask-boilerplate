from tests.api.v1 import TestBase


class TestAuth(TestBase):
	"""
	Tests auth endpoints: Login and register
	"""


	def test_ok_login_user(self):
		"""
		Tests if login an existing user is OK
		:return:
		"""
		data = {
			'email': self.u.email,
			'password': 'test',
		}
		response = self.client.post('api/v1/auth/login', json=data)
		self.assertEqual(response.status_code, 200)
		self.assertTrue('token' in response.json)

	def test_ko_login_notexisting_user(self):
		"""
		Tests if login a not existing user is a KO
		:return:
		"""
		response = self.client.post('api/v1/auth/login', json={'email': 'nope@test.com', 'password': 'bushdid911'})
		self.assertEqual(response.status_code, 401)

	def test_ko_login_bad_credentials(self):
		"""
		Tests if login an existing user with bad credentials is a KO
		:return:
		"""
		data = {
			'email': self.u.email,
			'password': 'bushdid911',
		}
		response = self.client.post('api/v1/auth/login', json=data)
		self.assertEqual(response.status_code, 401)

