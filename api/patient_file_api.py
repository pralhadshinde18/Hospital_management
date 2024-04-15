from fastapi import APIRouter, HTTPException
from typing import List
from service.patient_file_service import PatientFileService
from schema.patient_file_schema import PatientFileBase, GetPatientFile, PatientFileCreate

router = APIRouter()


@router.post("/patient_file/", response_model=PatientFileBase)
def create_patient_file(patient_file_data: PatientFileCreate):
    patient_file_service = PatientFileService()
    return patient_file_service.create_patient_file(patient_file_data)


@router.get("/patient_file/", response_model=List[GetPatientFile])
def get_patient_file():
    patient_file_service = PatientFileService()
    return patient_file_service.get_patient_file()


@router.put("/patient_file/{patient_file_id}", response_model=PatientFileBase)
def update_patient_file(patient_file_id: int, patient_file_data: PatientFileCreate):
    patient_file_service = PatientFileService()
    return patient_file_service.update_patient_file(patient_file_id, patient_file_data)


@router.delete("/patient_file/{patient_file_id}", response_model=GetPatientFile)
def delete_patient_file(patient_file_id: int):
    patient_file_service = PatientFileService()
    try:
        return patient_file_service.delete_patient_file(patient_file_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
