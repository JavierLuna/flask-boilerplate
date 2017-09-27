from flask import request

from app.api.v1 import api_v1, auth_v1
from app.api.v1.son.schemas import SonSchema
from app.api.v1.utils import paginate, detail, create, partialupdate, delete
from app.models.father import Father
from app.models.son import Son


@api_v1.route('/son', methods=['GET'])
@paginate(SonSchema)
def list_sons():
	return Son.query


@api_v1.route('/son/<int:id>', methods=['GET'])
@detail(SonSchema)
def detail_son(id):
	return Son.query.get_or_404(id)


def pair_with_father(son_object):
	request_json = request.get_json()
	if request_json['father']:
		son_object.father = Father.query.get_or_404(int(request_json['father']))


@api_v1.route('/son', methods=['POST'])
@auth_v1.login_required
@create(SonSchema, after_function=pair_with_father)
def create_son():
	pass


@api_v1.route('/son/<int:id>', methods=['PATCH'])
@auth_v1.login_required
@partialupdate(SonSchema)
def update_son(id):
	return Son.query.get_or_404(id)


@api_v1.route('/son/<int:id>', methods=['DELETE'])
@auth_v1.login_required
@delete
def delete_son(id):
	return Son.query.get_or_404(id)
