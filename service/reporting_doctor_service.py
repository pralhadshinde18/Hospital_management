from typing import List
from schema.reporting_doctor_schema import ReportingDoctorCreate, GetReportingDoctor
from repository.reporting_doctor_repo import ReportingDoctorRepository
from domain.reporting_doctor_domain import ReportingDoctorDomain


class ReportingDoctorService:
    def __init__(self):
        self.repo = ReportingDoctorRepository()

    def create_reporting_doctor(self, reporting_doctor_data: ReportingDoctorCreate) -> GetReportingDoctor:
        reporting_doctor_domain = ReportingDoctorDomain(reporting_doctor_data)
        return self.repo.create_reporting_doctor(reporting_doctor_domain)

    def get_reporting_doctor(self) -> List[GetReportingDoctor]:
        return self.repo.get_reporting_doctor()

    def update_reporting_doctor(self, reporting_doctor_id: int,
                                reporting_doctor_data: ReportingDoctorCreate) -> GetReportingDoctor:
        reporting_doctor_domain = ReportingDoctorDomain(reporting_doctor_data)
        return self.repo.update_reporting_doctor(reporting_doctor_id, reporting_doctor_domain)

    def delete_reporting_doctor(self, reporting_doctor_id: int) -> GetReportingDoctor:
        return self.repo.delete_reporting_doctor(reporting_doctor_id)
