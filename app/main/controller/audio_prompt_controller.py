from flask import request
from flask_restx import Resource

from ..util.dto import AudioPromptDto
from ..service.audio_prompt_service import (
    save_new_audio_prompt,
    get_an_audio_prompt,
)

api = AudioPromptDto.api
_audioprompt = AudioPromptDto.audio_prompt


@api.route('/')
class AudioPromptCreate(Resource):
    @api.expect(_audioprompt, validate=True)
    @api.response(201, 'Audio prompt successfully created.')
    @api.doc('Create a audio prompt')
    def post(self):
        """Create a audio prompt"""
        data = request.json
        return save_new_audio_prompt(data=data)


@api.route('/<audio_prompt>')
@api.param('audio_prompt', 'The audio prompt identifier')
@api.response(404, 'Audio prompt not found.')
class AudioPrompt(Resource):
    @api.doc('get a audio recoredr')
    @api.marshal_with(_audioprompt)
    def get(self, audio_prompt):
        """get audio prompt information given its identifier"""
        audioprompt = get_an_audio_prompt(audio_prompt)
        if not audioprompt:
            api.abort(404)
        else:
            return audioprompt
