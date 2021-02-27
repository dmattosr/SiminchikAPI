from flask import request
from flask_restx import Resource

from ..util.dto import AccountDto
from ..service.account_service import save_new_account
from ..service.account_service import get_an_account
from ..service.account_service import update_password


api = AccountDto.api
_account = AccountDto.account

@api.route('/')
class Account(Resource):
	@api.doc('Create a new account.')
	@api.expect(_account, validate=True)
	@api.response(201, 'Account successfully created.')
	def post(self):
		'''Create a new account'''
		data = request.json
		return save_new_account(data=data)
	
	@api.doc('Update password')
	@api.response(201, 'Password successfully changed.')
	def put(self,email,password):
		'''Update account\'s password'''
		return update_password(email,password)
	

@api.route('/<email>')
@api.param('email', 'The account identifier')
@api.response(404, 'Account not found.')
class AccountEmail(Resource):
	@api.doc('Get an account')
	@api.marshal_with(_account)
	def get(self, email):
		'''Get account\' information'''
		account = get_an_account(email)
		if not account:
			api.abort(404)
		else:
			return account