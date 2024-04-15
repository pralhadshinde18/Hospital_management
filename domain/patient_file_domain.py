from schema.patient_file_schema import PatientFileCreate


class PatientFileDomain:
    def __init__(self, patient_file_data: PatientFileCreate):
        self.validate(patient_file_data)
        self.patient_file_data = patient_file_data

    def validate(self, patient_file_data: PatientFileCreate):
        pass