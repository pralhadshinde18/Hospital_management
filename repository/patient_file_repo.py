from database import SessionLocal
from typing import List
from domain.patient_file_domain import PatientFileDomain
from schema.patient_file_schema import GetPatientFile
from model.patient_file_model import PatientFile


class PatientFileRepository:
    def create_patient_file(self, patient_file_domain: PatientFileDomain) -> GetPatientFile:
        db_patient_file = PatientFile(**patient_file_domain.patient_file_data.dict())
        db = SessionLocal()
        db.add(db_patient_file)
        db.commit()
        db.refresh(db_patient_file)
        db.close()
        return db_patient_file

    def get_patient_file(self) -> List[GetPatientFile]:
        db = SessionLocal()
        patient_files = db.query(PatientFile).all()
        db.close()
        return patient_files

    def update_patient_file(self, patient_file_id: int,
                            patient_file_domain: PatientFileDomain) -> GetPatientFile:
        db = SessionLocal()
        db_patient_file = db.query(PatientFile).filter(PatientFile.id == patient_file_id).first()
        if db_patient_file:
            update_data = patient_file_domain.patient_file_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_patient_file, key, value)
            db.commit()
            db.refresh(db_patient_file)
            db.close()
            return db_patient_file

    def delete_patient_file(self, patient_file_id: int) -> GetPatientFile:
        db = SessionLocal()
        db_patient_file = db.query(PatientFile).filter(PatientFile.id == patient_file_id).first()
        if db_patient_file:
            db.delete(db_patient_file)
            db.commit()
            db.close()
            return db_patient_file
        else:
            raise Exception("Patient File not found")
