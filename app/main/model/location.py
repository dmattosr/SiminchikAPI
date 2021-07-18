
from .. import db


class Country(db.Model):
    """ Country Model for storing area related details """
    __tablename__ = "country"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), default='', nullable=False)
    iso3 = db.Column(db.String(3), default='', nullable=False)
    iso2 = db.Column(db.String(2), default='', nullable=False)
    phone_code = db.Column(db.String(5), default='', nullable=False)
    currency = db.Column(db.String(10), default='', nullable=False)
    native = db.Column(db.String(100), default='', nullable=False)
    region = db.Column(db.String(100), default='', nullable=False)
    subregion = db.Column(db.String(100), default='', nullable=False)
    timezone = db.Column(db.String(20), default='', nullable=False)

    def __repr__(self):
        return "<Country '{}'>".format(self.name)


class State(db.Model):
    """ State Model for storing area related details """
    __tablename__ = "state"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), default='', nullable=False)
    state_code = db.Column(db.String(3), default='', nullable=False)

    def __repr__(self):
        return "<State '{}'>".format(self.name)


class City(db.Model):
    """ City Model for storing area related details """
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), default='', nullable=False)
    latitude = db.Column(db.String(50), default='', nullable=False)
    longitude = db.Column(db.String(50), default='', nullable=False)

    def __repr__(self):
        return "<City '{}'>".format(self.name)
