from typing import List
from fastapi import APIRouter, HTTPException
from schema.patient_schema import PatientBase,PatientCreate,GetPatientResponse
from service.patient_service import PatientService

router = APIRouter()


@router.post("/patient/", response_model=PatientBase)
def create_patient(patient_data: PatientCreate):
    patient_service = PatientService()
    return patient_service.create_patient(patient_data)


@router.get("/patient/", response_model=List[GetPatientResponse])
def get_all_patient():
    patient_service = PatientService()
    return patient_service.get_all_patients()


@router.put("/patient/{patient_id}", response_model=PatientBase)
def update_patient(patient_id: int, patient_data: PatientCreate):
    patient_service = PatientService()
    return patient_service.update_patient(patient_id, patient_data)


@router.delete("/patient/{patient_id}", response_model=GetPatientResponse)
def delete_patient(patient_id: int):
    patient_service = PatientService()
    try:
        return patient_service.delete_patient(patient_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
