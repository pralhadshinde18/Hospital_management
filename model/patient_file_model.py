from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class PatientFile(Base):
    __tablename__ = 'patient_file'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_name = Column(String(100))
    examine_date = Column(Date)
    report_status = Column(String(50))
    referred_doctor = Column(String(100))

    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("Patient", back_populates="patient_files")
    documents = relationship("Document", back_populates="patient_file")