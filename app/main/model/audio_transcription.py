
from .. import db


class Audio_transcription(db.Model):
    """
    Audio Transcription Model for storing prompts related details
    """
    __tablename__ = 'audio_transcription'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    dialect_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), default='', nullable=False)
    quality = db.Column(db.Integer, default=1, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Audio Transcription '{}'>".format(self.name)
