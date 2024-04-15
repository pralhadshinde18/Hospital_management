from database import SessionLocal
from typing import List
from schema.document_schema import GetDocumentResponse
from model.document_model import Document
from domain.document_domain import DocumentDomain

class DocumentRepository:
    def create_document(self, document_domain: DocumentDomain) -> GetDocumentResponse:
        db_document = Document(**document_domain.document_data.dict())
        db = SessionLocal()
        db.add(db_document)
        db.commit()
        db.refresh(db_document)
        db.close()
        return db_document

    def get_all_documents(self) -> List[GetDocumentResponse]:
        db = SessionLocal()
        documents = db.query(Document).all()
        db.close()
        return documents

    def update_document(self, document_id: int, document_domain: DocumentDomain) -> GetDocumentResponse:
        db = SessionLocal()
        db_document = db.query(Document).filter(Document.id == document_id).first()
        if db_document:
            update_data = document_domain.document_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_document, key, value)
            db.commit()
            db.refresh(db_document)
        db.close()
        return db_document

    def delete_document(self, document_id: int) -> GetDocumentResponse:
        db = SessionLocal()
        db_document = db.query(Document).filter(Document.id == document_id).first()
        if db_document:
            db.delete(db_document)
            db.commit()
            db.close()
            return db_document
        else:
            db.close()
            raise Exception("Document not found")
