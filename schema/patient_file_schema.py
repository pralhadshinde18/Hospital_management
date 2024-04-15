from pydantic import BaseModel
from datetime import date


class PatientFileBase(BaseModel):
    patient_name: str
    examine_date: date
    report_status: str
    referred_doctor: str


class PatientFileCreate(PatientFileBase):
    pass


class GetPatientFile(PatientFileBase):
    id: int

    class config:
        orm_mode = True
