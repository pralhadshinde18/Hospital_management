from schema.technician_schema import TechnicianCreate, GetTechnicianResponse
from domain.technician_domain import TechnicianDomain
from repository.technician_repo import TechnicianRepository
from typing import List


class TechnicianService:
    def __init__(self):
        self.repo = TechnicianRepository()

    def create_technician(self, technician_data: TechnicianCreate) -> GetTechnicianResponse:
        technician_domain = TechnicianDomain(technician_data)
        return self.repo.create_technician(technician_domain)

    def get_all_technician(self) -> List[GetTechnicianResponse]:
        return self.repo.get_all_technician()

    def update_technician(self, technician_id: int, technician_data: TechnicianCreate) -> GetTechnicianResponse:
        technician_domain = TechnicianDomain(technician_data)
        return self.repo.update_technician(technician_id, technician_domain)

    def delete_technician(self, technician_id: int) -> GetTechnicianResponse:
        return self.repo.delete_technician(technician_id)
