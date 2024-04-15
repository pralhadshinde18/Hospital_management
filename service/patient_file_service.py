from typing import List
from schema.patient_file_schema import PatientFileCreate, GetPatientFile
from domain.patient_file_domain import PatientFileDomain
from repository.patient_file_repo import PatientFileRepository


class PatientFileService:
    def __init__(self):
        self.repo = PatientFileRepository()

    def create_patient_file(self, patient_file_data: PatientFileCreate) -> GetPatientFile:
        patient_file_domain = PatientFileDomain(patient_file_data)
        return self.repo.create_patient_file(patient_file_domain)

    def get_patient_file(self) -> List[GetPatientFile]:
        return self.repo.get_patient_file()

    def update_patient_file(self, patient_file_id: int,
                            patient_file_data: PatientFileCreate) -> GetPatientFile:
        patient_file_domain = PatientFileDomain(patient_file_data)
        return self.repo.update_patient_file(patient_file_id, patient_file_domain)

    def delete_patient_file(self, patient_file_id: int) -> GetPatientFile:
        return self.repo.delete_patient_file(patient_file_id)