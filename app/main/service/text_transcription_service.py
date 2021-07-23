
import datetime

from app.main import db
from app.main.model.text_transcription import Text_transcription


def save_new_text_transcription(data):
    save_new_text_transcription = Text_transcription(
        audio_transcription_id=data['audio_transcription_id'],
        source_dialect_id=data['source_dialect_id'],
        dest_dialect_id=data['dest_dialect_id'],
        text_transcription=data['text_transcription'],
        quality=data['quality'],
        registered_on=datetime.datetime.utcnow(),
    )
    save_changes(save_new_text_transcription)
    return 201


def get_an_text_transcription(text_transcription_id):
    return Text_transcription.query.filter_by(id=text_transcription_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
