from functools import wraps

from flask import jsonify, request, current_app, abort
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app import db


def json(f):
	@wraps(f)
	def wrapped(*args, **kwargs):
		rv = f(*args, **kwargs)
		code = 200
		if isinstance(rv, tuple):
			code = rv[1]
			rv = rv[0]
		return jsonify(rv), code

	return wrapped


def paginate(schema):
	def inception(f):
		@wraps(f)
		def wrapped(*args, **kwargs):
			s = schema(many=True)
			page = request.args.get('page', 1, type=int)
			rv = f(*args, **kwargs)
			paginator = rv.paginate(page, per_page=current_app.config['RESULTS_PER_API_CALL'], error_out=False)
			resulting_data = {'objects': s.dump(paginator.items, many=True).data,
			                  'next_page': paginator.next_num if paginator.has_next else None,
			                  'prev_page': paginator.prev_num if paginator.has_prev else None,
			                  'pages': paginator.pages,
			                  'total_objects': paginator.total}
			return jsonify(resulting_data)

		return wrapped

	return inception


def detail(schema):
	def inception(f):
		@wraps(f)
		def wrapped(*args, **kwargs):
			s = schema()
			instance = f(*args, **kwargs)
			return jsonify(s.dump(instance).data)

		return wrapped

	return inception


def create(schema, after_function=None):
	def inception(f):
		@wraps(f)
		def wrapped(*args, **kwargs):
			s = schema()
			raw_data = request.get_json()
			result = s.load(raw_data)
			if result.errors:
				raise ValidationError(result.errors)
			new_object = result.data
			if after_function is not None:
				after_function(new_object)
			db.session.add(new_object)
			try:
				db.session.commit()
				return jsonify(s.dump(new_object).data), 201
			except IntegrityError:
				db.session.rollback()
				abort(500)

		return wrapped

	return inception


def partialupdate(schema, after_function=None):
	def inception(f):
		@wraps(f)
		def wrapped(*args, **kwargs):
			s = schema()
			raw_data = request.get_json()
			instance = f(*args, **kwargs)
			result = s.load(raw_data, instance=instance)
			if result.errors:
				raise ValidationError(result.errors)
			new_object = result.data
			if after_function is not None:
				after_function(new_object)
			return jsonify(s.dump(result.data).data)

		return wrapped

	return inception


def delete(f):
	@wraps(f)
	def wrapped(*args, **kwargs):
		instance = f(*args, **kwargs)
		db.session.delete(instance)
		db.session.commit()
		return '', 204

	return wrapped
