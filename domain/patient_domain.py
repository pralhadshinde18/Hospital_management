from schema.patient_schema import PatientCreate


class PatientDomain:
    def __init__(self, patient_data: PatientCreate):
        self.validate(patient_data)
        self.patient_data = patient_data

    def validate(self, patient_data: PatientCreate):
        if patient_data.contact_number < 1:
            raise ValueError("contact number must be greater than 1")