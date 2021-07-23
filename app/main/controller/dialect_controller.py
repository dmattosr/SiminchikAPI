from flask import request
from flask_restx import Resource

from ..util.dto import DialectDto
from ..service.language_service import (
    save_new_dialect,
    get_an_dialect,
)

api = DialectDto.api
_dialect = DialectDto.dialect


@api.route('/')
class DialectCreate(Resource):
    @api.expect(_dialect, validate=True)
    @api.response(201, 'Dialect successfully created.')
    @api.doc('Create a dialect')
    def post(self):
        """Create a language"""
        data = request.json
        return save_new_dialect(data=data)


@api.route('/<dialect_id>')
@api.param('dialect_id', 'The dialect identifier')
@api.response(404, 'Dialect not found.')
class Dialect(Resource):
    @api.doc('get a dialect')
    @api.marshal_with(_dialect)
    def get(self, dialect_id):
        """get dialect information given its identifier"""
        language = get_an_dialect(dialect_id)
        if not language:
            api.abort(404)
        else:
            return language
