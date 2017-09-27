from werkzeug.contrib.fixers import ProxyFix

from app import create_app

app = create_app(config_name='production')

# Fix to nginx reverse proxy issues (if any, uncomment commented lines)
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
	app.run()
