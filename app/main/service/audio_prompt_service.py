
import datetime

from app.main import db
from app.main.model.audio_prompt import Audio_prompt


def save_new_audio_prompt(data):
    new_audio_prompt = Audio_prompt(
        text_prompt_id=data['text_prompt_id'],
        user_id=data['user_id'],
        name=data['name'],
        changed_on=datetime.datetime.utcnow(),
        registered_on=datetime.datetime.utcnow(),
    )
    save_changes(new_audio_prompt)
    return 201


def get_an_audio_prompt(audio_prompt_id):
    return Audio_prompt.filter_by(id=audio_prompt_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
