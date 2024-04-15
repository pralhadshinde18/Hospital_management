from domain.technician_domain import TechnicianDomain
from schema.technician_schema import GetTechnicianResponse
from model.technician_model import Technician
from database import SessionLocal
from typing import List

class TechnicianRepository:
    def create_technician(self, technician_domain: TechnicianDomain) -> GetTechnicianResponse:
        db_technician = Technician(**technician_domain.technician_data.dict())
        db = SessionLocal()
        db.add(db_technician)
        db.commit()
        db.refresh(db_technician)
        db.close()
        return db_technician

    def get_all_technician(self) -> List[GetTechnicianResponse]:
        db = SessionLocal()
        technicians = db.query(Technician).all()
        db.close()
        return technicians

    def update_technician(self, technician_id: int, technician_domain: TechnicianDomain) -> GetTechnicianResponse:
        db = SessionLocal()
        db_technician = db.query(Technician).filter(Technician.id == technician_id).first()
        if db_technician:
            update_data = technician_domain.technician_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_technician, key, value)
            db.commit()
            db.refresh(db_technician)
        db.close()
        return db_technician

    def delete_technician(self, technician_id: int) -> GetTechnicianResponse:
        db = SessionLocal()
        db_technician = db.query(Technician).filter(Technician.id == technician_id).first()
        if db_technician:
            db.delete(db_technician)
            db.commit()
            db.close()
            return db_technician
        else:
            db.close()
            raise Exception("technician not found")