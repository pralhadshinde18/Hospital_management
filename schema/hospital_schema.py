from pydantic import BaseModel
from typing import List


class HospitalBase(BaseModel):
    hospital_name: str
    area: str
    description: str
    email_address: str
    rating: float
    contact_number: int
    whatsapp_number: int
    address: str
    category: str


class HospitalCreate(HospitalBase):
    pass


class GetHospitalResponse(HospitalBase):
    id: int

    class Config:
        orm_mode = True
