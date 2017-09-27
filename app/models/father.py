from app import db


class Father(db.Model):
	__tablename__ = "fathers"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)

	sons = db.relationship('Son', backref='father', lazy='dynamic')