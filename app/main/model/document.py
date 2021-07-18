
from .. import db


class Document(db.Model):
    """ Document Model for storing document ID related details """
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), default='', nullable=False)
    description = db.Column(db.String(100), default='', nullable=False)

    def __repr__(self):
        return "<Document '{}'>".format(self.name)
