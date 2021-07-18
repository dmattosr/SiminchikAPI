
from .. import db


class Language(db.Model):
    """ Language Model for storing user related details """
    __tablename__ = "language"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), default='', nullable=False)
    iso3 = db.Column(db.String(3), default='', nullable=False)

    def __repr__(self):
        return "<Language '{}'>".format(self.name)


class Dialect(db.Model):
    """ Language Model for storing user related details """
    __tablename__ = "dialect"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    language_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), default='', nullable=False)

    def __repr__(self):
        return "<Dialect '{}'>".format(self.name)
