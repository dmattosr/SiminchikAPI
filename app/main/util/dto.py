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


class CountryDto:
    api = Namespace('country', description='Country related operations')
    country = api.model('country', {
        'name': fields.String(required=True, description='Name'),
        'iso3': fields.String(description='ISO3'),
        'iso2': fields.String(description='ISO32'),
        'phone_code': fields.String(description='Phone de'),
        'currency': fields.String(description='Currency'),
        'native': fields.String(description='Native'),
        'region': fields.String(description='Región'),
        'subregion': fields.String(description='Subregion'),
        'timezone': fields.String(description='Timezone'),
        'text_prompt_id': fields.Integer(description='text prompt id'),
    })


class StateDto:
    api = Namespace('state', description='State related operations')
    state = api.model('state', {
        'country_id': fields.Integer(description='Country id'),
        'name': fields.String(required=True, description='State name'),
        'state_code': fields.String(required=True, description='State Code'),
    })


class CityDto:
    api = Namespace('city', description='City related operations')
    city = api.model('city', {
        'state_id': fields.Integer(description='City id'),
        'name': fields.String(description='City name'),
        'latitude': fields.String(required=True, description='Latitude'),
        'longitude': fields.String(required=True, description='Longitude'),
    })

# class AudioRecordedDto:
#     api = Namespace('audio_recorded', description='audio recorded related operations')
#     audio_recorder = api.model('audio_recorded', {
#         'text_prompt_id': fields.Integer(required=True, description='text prompt id'),
#         'user_id': fields.Integer(required=True, description='user id'),
#         'name': fields.String(required=True, description='name'),
#     })
