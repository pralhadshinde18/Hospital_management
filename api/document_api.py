from fastapi import APIRouter, HTTPException
from schema.document_schema import DocumentBase, GetDocumentResponse, DocumentCreate
from service.document_service import DocumentService
from typing import List

router = APIRouter()


@router.post("/document/", response_model=DocumentBase)
def create_document(document_data: DocumentCreate):
    document_service = DocumentService()
    return document_service.create_document(document_data)


@router.get("/document/", response_model=List[GetDocumentResponse])
def get_all_documents():
    document_service = DocumentService()
    return document_service.get_all_documents()


@router.put("/document/{document_id}", response_model=DocumentBase)
def update_document(document_id: int, document_data: DocumentCreate):
    document_service = DocumentService()
    return document_service.update_document(document_id, document_data)


@router.delete("/document/{document_id}", response_model=GetDocumentResponse)
def delete_document(document_id: int):
    document_service = DocumentService()
    try:
        return document_service.delete_document(document_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
