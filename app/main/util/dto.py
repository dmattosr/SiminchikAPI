from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'first_name': fields.String(required=True, description='user first_name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'type_doc_id': fields.Integer(required=True, description='user type_doc_id'),
        'num_doc': fields.String(required=True, description='user num_doc'),
        'country_id': fields.Integer(required=True, description='user country_id'),
        'state_id': fields.Integer(required=True, description='user state_id'),
        'city_id': fields.Integer(required=True, description='user city_id'),
        'dialect_id': fields.Integer(required=True, description='user dialect_id')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password_hash': fields.String(required=True, description='The user password ')
    })


class AccountDto:
    api = Namespace('account', description='account related operations')
    account = api.model('account', {
        'id_user': fields.Integer(required=True, description='account id_user'),
        'email': fields.String(required=True, description='account email'),
        'password_hash': fields.String(required=True, description='account password')
    })


class AudioPromptDto:
    api = Namespace('audio_prompt', description='audio prompt related operations')
    audio_prompt = api.model('audio_prompt', {
        'text_prompt_id': fields.Integer(required=True, description='text prompt id'),
        'user_id': fields.Integer(required=True, description='user id'),
        'name': fields.String(required=True, description='name'),
    })
