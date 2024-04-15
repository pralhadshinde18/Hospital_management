from schema.document_schema import DocumentCreate


class DocumentDomain:
    def __init__(self, document_data: DocumentCreate):
        self.validate(document_data)
        self.document_data = document_data

    def validate(self, patient_file_data: DocumentCreate):
        pass
