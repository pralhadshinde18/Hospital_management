from typing import List
from domain.hospital_domain import HospitalDomain
from repository.hospital_repo import HospitalRepository
from schema.hospital_schema import HospitalCreate, GetHospitalResponse


class HospitalService:
    def __init__(self):
        self.repo = HospitalRepository()

    def create_hospital(self, hospital_data: HospitalCreate) -> GetHospitalResponse:
        hospital_domain = HospitalDomain(hospital_data)
        return self.repo.create_hospital(hospital_domain)

    def get_all_hospitals(self) -> List[GetHospitalResponse]:
        return self.repo.get_all_hospitals()

    def update_hospital(self, hospital_id: int, hospital_data: HospitalCreate) -> GetHospitalResponse:
        hospital_domain = HospitalDomain(hospital_data)
        return self.repo.update_hospital(hospital_id, hospital_domain)

    def delete_hospital(self, hospital_id: int) -> GetHospitalResponse:
        return self.repo.delete_hospital(hospital_id)
