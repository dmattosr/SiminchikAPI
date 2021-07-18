
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(num_doc=data['num_doc']).first()
    if not user:
        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            type_doc_id=data['type_doc_id'],
            num_doc=data['num_doc'],
            country_id=data['country_id'],
            state_id=data['state_id'],
            city_id=data['city_id'],
            dialect_id=data['dialect_id'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_an_user(user_id):
    return User.query.filter_by(id=user_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
