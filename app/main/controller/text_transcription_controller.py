from flask import request
from flask_restx import Resource

from ..util.dto import TextTranscriptionDto
from ..service.text_transcription_service import (
    save_new_text_transcription,
    get_an_text_transcription,
)

api = TextTranscriptionDto.api
_texttranscription = TextTranscriptionDto.texttranscription


@api.route('/')
class TextTranscriptionCreate(Resource):
    @api.expect(_texttranscription, validate=True)
    @api.response(201, 'Text transcription successfully created.')
    @api.doc('Create a text transcription')
    def post(self):
        """Create a text transcription"""
        data = request.json
        return save_new_text_transcription(data=data)


@api.route('/<text_transcription_id>')
@api.param('get_an_text_transcription', 'The text transcription identifier')
@api.response(404, 'Text transcription not found.')
class TextTranscription(Resource):
    @api.doc('get a text transcription')
    @api.marshal_with(_texttranscription)
    def get(self, text_transcription_id):
        """get Text transcription information given its identifier"""
        text_transcription_id = get_an_text_transcription(text_transcription_id)
        if not text_transcription_id:
            api.abort(404)
        else:
            return text_transcription_id
