from typing import List
from domain.patient_domain import PatientDomain
from repository.patient_repo import PatientRepository
from schema.patient_schema import PatientCreate, GetPatientResponse


class PatientService:
    def __init__(self):
        self.repo = PatientRepository()

    def create_patient(self, patient_data: PatientCreate) -> GetPatientResponse:
        patient_domain = PatientDomain(patient_data)
        return self.repo.create_patient(patient_domain)

    def get_all_patients(self) -> List[GetPatientResponse]:
        return self.repo.get_all_patients()

    def update_patient(self, patient_id: int, patient_data: PatientCreate) -> GetPatientResponse:
        patient_domain = PatientDomain(patient_data)
        return self.repo.update_patient(patient_id, patient_domain)

    def delete_patient(self, patient_id: int) -> GetPatientResponse:
        return self.repo.delete_patient(patient_id)
