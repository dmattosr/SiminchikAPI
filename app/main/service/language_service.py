
from app.main import db
from app.main.model.language import Language, Dialect


def save_new_language(data):
    new_language = Language(
        name=data['name'],
        iso3=data['iso3'],
    )
    save_changes(new_language)
    return 201


def get_an_language(language_id):
    return Language.filter_by(id=language_id).first()


def save_new_dialect(data):
    new_dialect = Dialect(
        name=data['name'],
        iso3=data['iso3'],
    )
    save_changes(new_dialect)
    return 201


def get_an_dialect(dialect_id):
    return Dialect.filter_by(id=dialect_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
