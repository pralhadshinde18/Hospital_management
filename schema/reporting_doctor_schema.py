from pydantic import BaseModel
from datetime import date


class ReportingDoctorBase(BaseModel):
    user_name: str
    name: str
    address: str
    hospital_name: str
    contact_number: int
    whatsapp_number: int
    email_address: str
    education: str
    category: str
    speciality: str
    birth_date: date
    gender: str
    description: str
    hospital_id: int


class ReportingDoctorCreate(ReportingDoctorBase):
    pass


class GetReportingDoctor(ReportingDoctorBase):
    id: int

    class config:
        orm_mode = True
