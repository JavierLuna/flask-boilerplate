class ValidationError(Exception):
	def __init__(self, info):
		self.info = info