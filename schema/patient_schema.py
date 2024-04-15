from pydantic import BaseModel
from datetime import date


class PatientBase(BaseModel):
    name: str
    address: str
    contact_number: int
    whatsapp_number: int
    age: int
    gender: str
    birth_date: date
    reference_by: str
    test_conducted_by: str
    test_hospital: str
    referred_doctor: str
    referred_hospital: str
    clinical_category: str
    clinical_sub_category: str
    test: str
    format: str
    exam_procedure: str
    hospital_id: int


class PatientCreate(PatientBase):
    pass


class GetPatientResponse(PatientBase):
    id: int

    class Config:
        orm_mode = True
