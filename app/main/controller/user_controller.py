from flask import request
from flask_restx import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user
from ..service.user_service import get_an_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('Create a new user')
    def post(self):
        """Create a new User"""
        data = request.json
        return save_new_user(data=data)


@api.route('/<user_id>')
@api.param('user_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, user_id):
        """get user information given its identifier"""
        user = get_an_user(user_id)
        if not user:
            api.abort(404)
        else:
            return user
