from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.account_controller import api as account_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.audio_prompt_controller import api as audio_prompt_ns


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
