from repository.document_repo import DocumentRepository
from domain.document_domain import DocumentDomain
from schema.document_schema import GetDocumentResponse, DocumentCreate
from typing import List


class DocumentService:
    def __init__(self):
        self.repo = DocumentRepository()

    def create_document(self, document_data: DocumentCreate) -> GetDocumentResponse:
        document_domain = DocumentDomain(document_data)
        return self.repo.create_document(document_domain)

    def get_all_documents(self) -> List[GetDocumentResponse]:
        return self.repo.get_all_documents()

    def update_document(self, document_id: int, document_data: DocumentCreate) -> GetDocumentResponse:
        document_domain = DocumentDomain(document_data)
        return self.repo.update_document(document_id, document_domain)

    def delete_document(self, document_id: int) -> GetDocumentResponse:
        return self.repo.delete_document(document_id)
