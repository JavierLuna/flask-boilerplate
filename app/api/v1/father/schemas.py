from app import ma
from app.models.father import Father


class FatherSchema(ma.ModelSchema):
	class Meta:
		model = Father
		dump_only = ('id',)
		exclude = ('sons',)
