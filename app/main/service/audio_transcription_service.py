
import datetime

from app.main import db
from app.main.model.audio_transcription import Audio_transcription


def save_new_audio_transcription(data):
    new_audio_transcription = Audio_transcription(
        user_id=data['user_id'],
        dialect_id=data['dialect_id'],
        name=data['name'],
        quality=data['quality'],
        changed_on=datetime.datetime.utcnow(),
    )
    save_changes(new_audio_transcription)
    return 201


def get_an_audio_transcription(audio_transcription_id):
    return Audio_transcription.query.filter_by(id=audio_transcription_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
