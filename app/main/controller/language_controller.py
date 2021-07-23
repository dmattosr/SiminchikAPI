from flask import request
from flask_restx import Resource

from ..util.dto import LanguageDto
from ..service.language_service import (
    save_new_language,
    get_an_language,
)

api = LanguageDto.api
_language = LanguageDto.language


@api.route('/')
class LanguageCreate(Resource):
    @api.expect(_language, validate=True)
    @api.response(201, 'Language successfully created.')
    @api.doc('Create a language')
    def post(self):
        """Create a language"""
        data = request.json
        return save_new_language(data=data)


@api.route('/<language_id>')
@api.param('language_id', 'The language identifier')
@api.response(404, 'Language not found.')
class Language(Resource):
    @api.doc('get a language')
    @api.marshal_with(_language)
    def get(self, language_id):
        """get language information given its identifier"""
        language = get_an_language(language_id)
        if not language:
            api.abort(404)
        else:
            return language
