from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Date
from database import Base
from sqlalchemy.orm import relationship
from model.patient_hospital_link import patient_hospital_link


class Patient(Base):
    __tablename__ = 'patient'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100))
    address = Column(String(100))
    contact_number = Column(Integer)
    whatsapp_number = Column(Integer)
    age = Column(Integer)
    gender = Column(String(10))
    birth_date = Column(Date)
    reference_by = Column(String(100))
    test_conducted_by = Column(String(100))
    test_hospital = Column(String(50))
    referred_doctor = Column(String(50))
    referred_hospital = Column(String(100))
    clinical_category = Column(String(100))
    clinical_sub_category = Column(String(20))
    test = Column(String(50))
    format = Column(String(50))
    exam_procedure = Column(String(50))
    hospital_id = Column(Integer, ForeignKey('hospital.id'))

    hospitals = relationship("Hospital",secondary=patient_hospital_link,back_populates="patients")
    patient_files = relationship("PatientFile", back_populates="patient")
