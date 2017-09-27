from flask import jsonify

from . import views

@views.errorhandler(400)
def cuatrocientosuno():
	return jsonify({"code": 401, "message": "Not allowed"})