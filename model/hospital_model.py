from sqlalchemy import Integer, Column, String, Float
from database import Base
from sqlalchemy.orm import relationship
from model.patient_hospital_link import patient_hospital_link


class Hospital(Base):
    __tablename__ = 'hospital'
    id = Column(Integer, autoincrement=True, primary_key=True)
    hospital_name = Column(String(100), nullable=False)
    area = Column(String(100), nullable=False)
    description = Column(String(100))
    email_address = Column(String(100))
    rating = Column(Float)
    contact_number = Column(Integer)
    whatsapp_number = Column(Integer)
    address = Column(String(100))
    category = Column(String(100))

    technicians = relationship("Technician", back_populates="hospital")
    reporting_doctors = relationship("ReportingDoctor", back_populates="hospital")
    patients = relationship("Patient", secondary=patient_hospital_link, back_populates="hospitals")
