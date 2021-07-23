
from .. import db


class Audio_prompt(db.Model):
    """
    Audio Prompt Model for storing text-prompts related details
    """
    __tablename__ = "audio_prompt"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), default='', nullable=False)
    changed_on = db.Column(db.DateTime, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Audio Prompt '{}'>".format(self.id_achievement)
