
from .. import db


class Text_transcription(db.Model):
    """
    Text transcription Model for storing user related details
    """
    __tablename__ = "text_prompt"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    audio_transcription_id = db.Column(db.Integer, nullable=False)
    source_dialect_id = db.Column(db.Integer, nullable=False)
    dest_dialect_id = db.Column(db.Integer, nullable=False)
    text_transcription = db.Column(db.String(2000), default='', nullable=False)
    quality = db.Column(db.Integer, default=1, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Text transcription '{}'>".format(self.text_transcription)
