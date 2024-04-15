from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String)
    is_downloaded = Column(Boolean)

    patient_file_id = Column(Integer, ForeignKey('patient_file.id'))
    patient_file = relationship("PatientFile", back_populates="documents")