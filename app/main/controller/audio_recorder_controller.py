from flask import request
from flask_restx import Resource

from ..util.dto import AudioRecorderDto
from ..service.audio_recorder_service import (
    save_new_audio_recorder,
    get_an_audio_recorder,
)

api = AudioRecorderDto.api
_audiorecorder = AudioRecorderDto.audio_recorder


@api.route('/')
class AudioRecorderCreate(Resource):
    @api.expect(_audiorecorder, validate=True)
    @api.response(201, 'Audio recorder successfully created.')
    @api.doc('Create a audio recorder')
    def post(self):
        """Create a audio recorder"""
        data = request.json
        return save_new_audio_recorder(data=data)


@api.route('/<audio_recorder_id>')
@api.param('audio_recorder_id', 'The audio recorder identifier')
@api.response(404, 'Audio recorder not found.')
class AudioRecorder(Resource):
    @api.doc('get a audio recorder')
    @api.marshal_with(_audiorecorder)
    def get(self, audio_recorder_id):
        """get audio recorder information given its identifier"""
        audioprompt = get_an_audio_recorder(audio_recorder_id)
        if not audioprompt:
            api.abort(404)
        else:
            return audioprompt
