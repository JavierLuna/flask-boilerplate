from app.api.v1 import api_v1, auth_v1
from app.api.v1.father.schemas import FatherSchema
from app.api.v1.utils import paginate, detail, create, partialupdate, delete
from app.models.father import Father


@api_v1.route('/father', methods=['GET'])
@paginate(FatherSchema)
def list_fathers():
	return Father.query


@api_v1.route('/father/<int:id>', methods=['GET'])
@detail(FatherSchema)
def detail_father(id):
	return Father.query.get_or_404(id)


@api_v1.route('/father', methods=['POST'])
@auth_v1.login_required
@create(FatherSchema)
def create_father():
	pass


@api_v1.route('/father/<int:id>', methods=['PATCH'])
@auth_v1.login_required
@partialupdate(FatherSchema)
def update_father(id):
	return Father.query.get_or_404(id)


@api_v1.route('/father/<int:id>', methods=['DELETE'])
@auth_v1.login_required
@delete
def delete_father(id):
	return Father.query.get_or_404(id)
