import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	RESULTS_PER_API_CALL = 25


	@staticmethod
	def init_app(app):
		"""
		If some configuration needs to initialize the app in some way use this function
		:param app: Flask app
		:return:
		"""
		pass


class DevelopmentConfig(Config):
	DEBUG = False
	SECRET_KEY = os.environ.get('SECRET_KEY') or "hunter02"
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	                          'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
	TESTING = True
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_COMMIT_ON_TEARDOWN = False
	SECRET_KEY = os.environ.get('SECRET_KEY') or "hunter02"
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
	                          'sqlite:///:memory:'



class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')



config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}
