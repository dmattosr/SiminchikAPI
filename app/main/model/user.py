
from .. import db
import datetime

class User(db.Model):
	""" User Model for storing user related details """
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)	
	first_name = db.Column(db.String(100), default='', nullable=False)
	last_name = db.Column(db.String(100), default='', nullable=False)
	type_doc_id = db.Column(db.Integer, nullable=False)
	num_doc = db.Column(db.String(50), unique=True, nullable=False)
	country_id = db.Column(db.Integer, nullable=False)
	state_id = db.Column(db.Integer, nullable=False)
	city_id = db.Column(db.Integer, nullable=False)
	dialect_id = db.Column(db.Integer, nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)

	def __repr__(self):
		return "<User '{}'>".format(self.num_doc)