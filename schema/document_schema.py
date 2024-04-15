from pydantic import BaseModel


class DocumentBase(BaseModel):
    file_name: str
    is_downloaded: bool
    patient_file_id: int


class DocumentCreate(DocumentBase):
    pass


class GetDocumentResponse(DocumentBase):
    id: int

    class Config:
        orm_mode = True