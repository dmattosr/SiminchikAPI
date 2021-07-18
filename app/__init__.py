from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.account_controller import api as account_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.audio_prompt_controller import api as audio_prompt_ns
from .main.controller.audio_recorder_controller import api as audio_recorder_ns
from .main.controller.audio_transcription_controller import api as audio_transcription_ns
from .main.controller.country_controller import api as location_country_ns
from .main.controller.state_controller import api as location_state_ns
from .main.controller.city_controller import api as location_city_ns
from .main.controller.document_controller import api as document_ns
from .main.controller.language_controller import api as language_ns
from .main.controller.dialect_controller import api as dialect_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Siminchik API',
          version='1.0',
          description='Siminchikkunarayku para la retilización y democratización de las lenguas de América.'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(account_ns, path='/account')
api.add_namespace(audio_prompt_ns, path='/audio_prompt')
api.add_namespace(audio_recorder_ns, path='/audio_recorder')
api.add_namespace(audio_transcription_ns, path='/audio_transcription')
api.add_namespace(location_country_ns, path='/location/country')
api.add_namespace(location_state_ns, path='/location/state')
api.add_namespace(location_city_ns, path='/location/city')
api.add_namespace(document_ns, path='/document')
api.add_namespace(language_ns, path='/language')
api.add_namespace(dialect_ns, path='/dialect')
