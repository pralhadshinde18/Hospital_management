from pydantic import BaseModel
from datetime import date


class TechnicianBase(BaseModel):
    user_name: str
    name: str
    hospital_name: str
    address: str
    contact_number: int
    whatsapp_number: int
    email_address: str
    education: str
    birth_date: date
    gender: str
    description: str
    hospital_id: int


class TechnicianCreate(TechnicianBase):
    pass


class GetTechnicianResponse(TechnicianBase):
    id: int

    class Config:
        orm_mode = True
