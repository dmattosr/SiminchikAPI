from flask import request
from flask_restx import Resource

from ..util.dto import TextPromptDto
from ..service.text_prompt_service import (
    save_new_text_prompt,
    get_an_text_prompt,
)

api = TextPromptDto.api
_textprompt = TextPromptDto.textprompt


@api.route('/')
class TextPromptCreate(Resource):
    @api.expect(_textprompt, validate=True)
    @api.response(201, 'Text Prompt successfully created.')
    @api.doc('Create a text prompt')
    def post(self):
        """Create a text prompt"""
        data = request.json
        return save_new_text_prompt(data=data)


@api.route('/<text_prompt_id>')
@api.param('get_an_text_prompt', 'The text prompt identifier')
@api.response(404, 'Text prompt not found.')
class TextPrompt(Resource):
    @api.doc('get a text prompt')
    @api.marshal_with(_textprompt)
    def get(self, text_prompt_id):
        """get Text prompt information given its identifier"""
        text_prompt = get_an_text_prompt(text_prompt_id)
        if not text_prompt:
            api.abort(404)
        else:
            return text_prompt
