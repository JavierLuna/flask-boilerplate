import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db
from app.models.user import User

app = create_app(os.getenv('ENV_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
	def clear():
		[print() for _ in range(100)]

	def db_add(o):
		db.session.add(o)
		db.session.commit()

	def flush():
		db.session.rollback()

	return dict(app=app, db=db, db_add=db_add, flush=flush, clear=clear, User=User)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
