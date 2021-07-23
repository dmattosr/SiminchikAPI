
from app.main import db
from app.main.model.document import Document


def save_new_document(data):
    new_document = Document(
        name=data['name'],
        description=data['description'],
    )
    save_changes(new_document)
    return 201


def get_an_document(document_id):
    return Document.query.filter_by(id=document_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
