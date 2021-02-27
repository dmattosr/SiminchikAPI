import uuid
import datetime

from app.main import db
from app.main.model.account import Account


def save_new_account(data):
	account = Account.query.filter_by(email=data['email']).first()
	if not account:
		new_account = Account(
			id_user = data['id_user'],
			email = data['email'],
			password_hash = data['password_hash'],
			old_password = data['password_hash'],
			wrong_login_attempt = 0,
			today_login_attempt = 0,
			is_now_login = 0,
			registered_on = datetime.datetime.utcnow()
		)        
		save_changes(new_account)
		return generate_token(new_account)
	else:
		response_object = {
			'status': 'Fail',
			'message': 'Account already exists. Please Log in.',
		}
		return response_object, 409


def get_an_account(email):
	return Account.query.filter_by(email = email).first()


def update_password(email,password):
	account = Account.query.filter_by(email = email).first()
	print(account)
	account.old_password = password
	account.password_hash = password
	db.session.commit()
	return 201

def generate_token(account):
	try:
		# generate the auth token
		auth_token = Account.encode_auth_token(account.id)
		response_object = {
			'status': 'success',
			'message': 'Successfully registered.',
			'Authorization': auth_token.decode()
		}
		return response_object, 201
	except Exception as e:
		response_object = {
			'status': 'fail',
			'message': 'Some error occurred. Please try again.'
		}
		return response_object, 401

def save_changes(data):
	db.session.add(data)
	db.session.commit()

