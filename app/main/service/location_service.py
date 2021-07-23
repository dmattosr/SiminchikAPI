
from app.main import db
from app.main.model.location import Country, State, City


# ########## Country
def save_new_country(data):
    country = Country.query.filter_by(name=data['name']).first()
    if not country:
        new_country = Country(
            name=data['name'],
            iso3=data['iso3'],
            iso2=data['iso2'],
            phone_code=data['phone_code'],
            currency=data['currency'],
            native=data['native'],
            region=data['region'],
            subregion=data['subregion'],
            timezone=data['timezone'],
        )
        save_changes(new_country)
        return 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Country already exists. Please Log in.',
        }
        return response_object, 409


def get_an_country(country_id):
    return Country.query.filter_by(id=country_id).first()


# ########## State
def save_new_state(data):
    state = State.query.filter_by(state_code=data['state_code']).first()
    if not state:
        new_state = State(
            country_id=data['country_id'],
            name=data['name'],
            state_code=data['state_code'],
        )
        save_changes(new_state)
        return 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'State already exists. Please Log in.',
        }
        return response_object, 409


def get_an_state(state_id):
    return State.query.filter_by(id=state_id).first()


# ########## City
def save_new_city(data):
    city = City.query.filter_by(state_id=data['state_id'], name=data['name']).first()
    if not city:
        new_city = City(
            state_id=data['state_id'],
            name=data['name'],
            latitude=data['latitude'],
            longitude=data['longitude'],
        )
        save_changes(new_city)
        return 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'City already exists. Please Log in.',
        }
        return response_object, 409


def get_an_city(state_id):
    return City.query.filter_by(id=state_id).first()



# ##########
def save_changes(data):
    db.session.add(data)
    db.session.commit()
