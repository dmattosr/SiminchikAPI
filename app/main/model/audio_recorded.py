
from .. import db
import datetime

class Audio_recorded(db.Model):
	"""
	Audio Recorded Model for storing audio related details
	"""
	__tablename__ = "audio_recorded"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	user_id = db.Column(db.Integer, nullable=False)	
	audio_prompt_id = b.Column(db.Integer, nullable=False)
	dialect_id = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(100), default='', nullable=False)
	quality = db.Column(db.Integer, default= 1, nullable=False)
	changed_on = db.Column(db.DateTime, nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)
	
	def __repr__(self):
		return "<Audio Recorded '{}'>".format(self.name)
