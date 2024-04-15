from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy import Date
from sqlalchemy.orm import relationship


class Technician(Base):
    __tablename__ = 'technician'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_name = Column(String(100))
    name = Column(String(100))
    hospital_name = Column(String(100))
    address = Column(String(100))
    contact_number = Column(Integer)
    whatsapp_number = Column(Integer)
    email_address = Column(String(100))
    education = Column(String(100))
    birth_date = Column(Date)
    gender = Column(String(10))
    description = Column(String(200))

    hospital_id = Column(Integer, ForeignKey('hospital.id'))
    hospital = relationship("Hospital", back_populates="technicians")
