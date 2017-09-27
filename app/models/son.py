from app import db

class Son(db.Model):
	__tablename__ = "sons"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150))

	father_id = db.Column(db.Integer, db.ForeignKey('fathers.id'))