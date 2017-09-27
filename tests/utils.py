import json as _json


class APITestClient:
	def __init__(self, test_client):
		self.test_client = test_client
		self.token = None

	def get_api_headers(self, token=None):
		headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json'
		}
		if self.token or token:
			headers['Authorization'] = "Token " + (token or self.token)
		return headers

	def get(self, url, token=None):
		response = self.test_client.get(url, headers=self.get_api_headers(token=token))
		return SimpleResponse(response.data, headers=response.headers, status_code=response.status_code)

	def post(self, url, json=None, token=None):
		json = _json.dumps(json) if json else None
		response = self.test_client.post(url, data=json, headers=self.get_api_headers(token=token))
		return SimpleResponse(response.data, headers=response.headers, status_code=response.status_code)

	def put(self, url, json=None, token=None):
		json = _json.dumps(json) if json else None
		response = self.test_client.put(url, data=json, headers=self.get_api_headers(token=token))
		return SimpleResponse(response.data, headers=response.headers, status_code=response.status_code)

	def patch(self, url, json=None, token=None):
		json = _json.dumps(json) if json else None
		response = self.test_client.patch(url, data=json, headers=self.get_api_headers(token=token))
		return SimpleResponse(response.data, headers=response.headers, status_code=response.status_code)

	def delete(self, url, token=None):
		response = self.test_client.delete(url, headers=self.get_api_headers(token=token))
		return SimpleResponse(response.data, headers=response.headers, status_code=response.status_code)


class SimpleResponse():
	def __init__(self, data, headers=None, status_code=None):
		self.data = data.decode('utf-8')
		self.headers = headers
		self.status_code = status_code
		self.__json_data = None

	@property
	def json(self):
		if not self.__json_data:
			self.__json_data = _json.loads(self.data)
		return self.__json_data
