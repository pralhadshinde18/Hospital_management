from sqlalchemy import Table, Column, Integer, ForeignKey
from database import Base

patient_hospital_link = Table('patient_hospital_link', Base.metadata,
                              Column('hospital_id', Integer, ForeignKey('hospital.id')),
                              Column('patient_id', Integer, ForeignKey('patient.id'))
                              )
