from flask import request
from flask_restx import Resource

from ..util.dto import DocumentDto
from ..service.document_service import (
    save_new_document,
    get_an_document,
)

api = DocumentDto.api
_document = DocumentDto.document


@api.route('/')
class DocumentCreate(Resource):
    @api.expect(_document, validate=True)
    @api.response(201, 'Document successfully created.')
    @api.doc('Create a document')
    def post(self):
        """Create a document"""
        data = request.json
        return save_new_document(data=data)


@api.route('/<document_id>')
@api.param('document_id', 'The document identifier')
@api.response(404, 'Document not found.')
class Document(Resource):
    @api.doc('get a document')
    @api.marshal_with(_document)
    def get(self, document_id):
        """get document information given its identifier"""
        document = get_an_document(document_id)
        if not document:
            api.abort(404)
        else:
            return document
