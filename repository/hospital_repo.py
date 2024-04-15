from typing import List
from domain.hospital_domain import HospitalDomain
from model.hospital_model import Hospital
from schema.hospital_schema import GetHospitalResponse
from database import SessionLocal


class HospitalRepository:
    def create_hospital(self, hospital_domain: HospitalDomain) -> GetHospitalResponse:
        db_hospital = Hospital(**hospital_domain.hospital_data.dict())
        db = SessionLocal()
        db.add(db_hospital)
        db.commit()
        db.refresh(db_hospital)
        db.close()
        return db_hospital

    def get_all_hospitals(self) -> List[GetHospitalResponse]:
        db = SessionLocal()
        hospitals = db.query(Hospital).all()
        db.close()
        return hospitals

    def update_hospital(self, hospital_id: int, hospital_domain: HospitalDomain) -> GetHospitalResponse:
        db = SessionLocal()
        db_hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
        if db_hospital:
            update_data = hospital_domain.hospital_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_hospital, key, value)
            db.commit()
            db.refresh(db_hospital)
        db.close()
        return db_hospital

    def delete_hospital(self, hospital_id: int) -> GetHospitalResponse:
        db = SessionLocal()
        db_hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
        if db_hospital:
            db.delete(db_hospital)
            db.commit()
            db.close()
            return db_hospital
        else:
            db.close()
            raise Exception("Hospital not found")
