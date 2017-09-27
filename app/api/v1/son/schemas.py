from marshmallow import fields

from app import ma
from app.api.v1.father.schemas import FatherSchema
from app.models.son import Son


class SonSchema(ma.ModelSchema):
	father = fields.Nested(FatherSchema, dump_only=True)

	class Meta:
		model = Son
		dump_only = ('id',)
