
from .. import db


class Text_prompt(db.Model):
    """
    Text Prompt Model for storing user related details
    """
    __tablename__ = "text_prompt"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dialect_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(2000), default='', nullable=False)
    source = db.Column(db.String(200), default='', nullable=False)
    changed_on = db.Column(db.DateTime, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Text Prompt '{}'>".format(self.text)
