from fastapi import FastAPI
from api.hospital_api import router as hospital_router
from api.technician_api import router as technician_router
from api.reporting_doctor_api import router as reporting_doctor_router
from api.patient_api import router as patient_router
from api.patient_file_api import router as patient_file_router
from api.document_api import router as document_router

app = FastAPI()

app.include_router(hospital_router)

app.include_router(technician_router)

app.include_router(reporting_doctor_router)

app.include_router(patient_router)

app.include_router(patient_file_router)

app.include_router(document_router)