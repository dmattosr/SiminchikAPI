from flask import request
from flask_restx import Resource

from ..util.dto import AudioTranscriptionDto
from ..service.audio_transcription_service import (
    save_new_audio_transcription,
    get_an_audio_transcription,
)

api = AudioTranscriptionDto.api
_audiotranscription = AudioTranscriptionDto.audio_transcription


@api.route('/')
class AudioTranscriptionCreate(Resource):
    @api.expect(_audiotranscription, validate=True)
    @api.response(201, 'Audio transcription successfully created.')
    @api.doc('Create a audio transcription')
    def post(self):
        """Create a audio transcription"""
        data = request.json
        return save_new_audio_transcription(data=data)


@api.route('/<audio_transcription_id>')
@api.param('audio_transcription_id', 'The audio transcription identifier')
@api.response(404, 'Audio transcription not found.')
class AudioTranscription(Resource):
    @api.doc('get a audio transcription')
    @api.marshal_with(_audiotranscription)
    def get(self, audio_transcription_id):
        """get audio transcription information given its identifier"""
        audiotranscription = get_an_audio_transcription(audio_transcription_id)
        if not audiotranscription:
            api.abort(404)
        else:
            return audiotranscription
