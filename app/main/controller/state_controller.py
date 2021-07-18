from flask import request
from flask_restx import Resource

from ..util.dto import (
    StateDto,
)

from ..service.location_service import (
    save_new_state,
    get_an_state,
)


api = StateDto.api
_state = StateDto.state


@api.route('/')
class StateCreate(Resource):
    @api.expect(_state, validate=True)
    @api.response(201, 'State successfully created.')
    @api.doc('Create a state')
    def post(self):
        """Create a state"""
        data = request.json
        return save_new_state(data=data)


@api.route('/<state_id>')
@api.param('state_id', 'The state identifier')
@api.response(404, 'State not found.')
class State(Resource):
    @api.doc('Get a state')
    @api.marshal_with(_state)
    def get(self, state_id):
        """get State information given its identifier"""
        state = get_an_state(state_id)
        if not state:
            api.abort(404)
        else:
            return state
