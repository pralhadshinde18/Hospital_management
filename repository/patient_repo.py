from typing import List
from database import SessionLocal
from domain.patient_domain import PatientDomain
from model.patient_model import Patient
from schema.patient_schema import GetPatientResponse


class PatientRepository:
    def create_patient(self, patient_domain: PatientDomain) -> GetPatientResponse:
        db_patient = Patient(**patient_domain.patient_data.dict())
        db = SessionLocal()
        db.add(db_patient)
        db.commit()
        db.refresh(db_patient)
        db.close()
        return db_patient

    def get_all_patients(self) -> List[GetPatientResponse]:
        db = SessionLocal()
        patients = db.query(Patient).all()
        db.close()
        return patients

    def update_patient(self, patient_id: int, patient_domain: PatientDomain) -> GetPatientResponse:
        db = SessionLocal()
        db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if db_patient:
            update_data = patient_domain.patient_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_patient, key, value)
            db.commit()
            db.refresh(db_patient)
        db.close()
        return db_patient

    def delete_patient(self, patient_id: int) -> GetPatientResponse:
        db = SessionLocal()
        db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if db_patient:
            db.delete(db_patient)
            db.commit()
            db.close()
            return db_patient
        else:
            db.close()
            raise Exception("Patient not found")
