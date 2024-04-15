from domain.reporting_doctor_domain import ReportingDoctorDomain
from schema.reporting_doctor_schema import GetReportingDoctor
from model.reporting_doctor_model import ReportingDoctor
from database import SessionLocal
from typing import List


class ReportingDoctorRepository:
    def create_reporting_doctor(self, reporting_doctor_domain: ReportingDoctorDomain) -> GetReportingDoctor:
        db_rep_doc = ReportingDoctor(**reporting_doctor_domain.reporting_doctor_data.dict())
        db = SessionLocal()
        db.add(db_rep_doc)
        db.commit()
        db.refresh(db_rep_doc)
        db.close()
        return db_rep_doc

    def get_reporting_doctor(self) -> List[GetReportingDoctor]:
        db = SessionLocal()
        reporting_doctor = db.query(ReportingDoctor).all()
        db.close()
        return reporting_doctor

    def update_reporting_doctor(self, reporting_doctor_id: int,
                                reporting_doctor_domain: ReportingDoctorDomain) -> GetReportingDoctor:
        db = SessionLocal()
        db_repo_doc = db.query(ReportingDoctor).filter(ReportingDoctor.id == reporting_doctor_id).first()
        if db_repo_doc:
            update_data = reporting_doctor_domain.reporting_doctor_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_repo_doc, key, value)
            db.commit()
            db.refresh(db_repo_doc)
            db.close()
            return db_repo_doc

    def delete_reporting_doctor(self, reporting_doctor_id: int) -> GetReportingDoctor:
        db = SessionLocal()
        db_repo_doc = db.query(ReportingDoctor).filter(ReportingDoctor.id == reporting_doctor_id).first()
        if db_repo_doc:
            db.delete(db_repo_doc)
            db.commit()
            db.close()
            return db_repo_doc
        else:
            return Exception("Reporting Doctor not found")
