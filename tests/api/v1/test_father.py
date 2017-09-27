from tests.api.v1 import TestBase


class TestFather(TestBase):
	"""
	Tests Father endpoints
	"""



	def test_ok_create(self):
		"""
		Tests if creating a Father is OK
		:return:
		"""
		data = {
			'name': 'Father test'
		}
		response = self.client.post('api/v1/father', json=data)
		self.assertEqual(response.status_code, 201)

	def test_ok_detail(self):
		"""
		Tests if giving detail of a Father is OK
		:return:
		"""
		data = {
			'name': 'Father test'
		}
		response = self.client.post('api/v1/father', json=data)
		self.assertEqual(response.status_code, 201)
		response = self.client.get('api/v1/father/1')
		self.assertEqual(response.status_code, 200)

	def test_ok_update(self):
		"""
		Tests if updating a Father is OK
		:return:
		"""
		data = {
			'name': 'Father test'
		}
		response = self.client.post('api/v1/father', json=data)
		self.assertEqual(response.status_code, 201)
		data['name'] = 'Father2 test'
		response = self.client.patch('api/v1/father/1', json=data)
		self.assertEqual(response.status_code, 200)
		self.assertTrue(response.json['name'] == data['name'])

	def test_ok_delete(self):
		"""
		Tests if deleting a Father is OK
		:return:
		"""
		data = {
			'name': 'Father test'
		}
		response = self.client.post('api/v1/father', json=data)
		self.assertEqual(response.status_code, 201)
		response = self.client.delete('api/v1/father/1')
		self.assertEqual(response.status_code, 204)
