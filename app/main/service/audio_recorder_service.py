
import datetime

from app.main import db
from app.main.model.audio_recorded import Audio_recorded


def save_new_audio_recorder(data):
    new_audio_recorder = Audio_recorded(
        user_id=data['user_id'],
        audio_prompt_id=data['audio_prompt_id'],
        dialect_id=data['dialect_id'],
        name=data['name'],
        quality=data['quality'],
        changed_on=datetime.datetime.utcnow(),
        registered_on=datetime.datetime.utcnow(),
    )
    save_changes(new_audio_recorder)
    return 201


def get_an_audio_recorder(audio_prompt_id):
    return Audio_recorded.filter_by(id=audio_prompt_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
