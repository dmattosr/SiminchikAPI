
import datetime

from app.main import db
from app.main.model.text_prompt import Text_prompt


def save_new_text_prompt(data):
    new_text_prompt = Text_prompt(
        dialect_id=data['dialect_id'],
        text=data['text'],
        source=data['source'],
        changed_on=datetime.datetime.utcnow(),
        registered_on=datetime.datetime.utcnow(),
    )
    save_changes(new_text_prompt)
    return 201


def get_an_text_prompt(text_prompt_id):
    return Text_prompt.filter_by(id=text_prompt_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
