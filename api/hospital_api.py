from typing import List
from fastapi import APIRouter, HTTPException
from schema.hospital_schema import HospitalBase, HospitalCreate, GetHospitalResponse
from service.hospital_service import HospitalService

router = APIRouter()


@router.post("/hospital/", response_model=HospitalBase)
def create_hospital(hospital_data: HospitalCreate):
    hospital_service = HospitalService()
    return hospital_service.create_hospital(hospital_data)


@router.get("/hospital/", response_model=List[GetHospitalResponse])
def get_all_hospitals():
    hospital_service = HospitalService()
    return hospital_service.get_all_hospitals()


@router.put("/hospital/{hospital_id}", response_model=HospitalBase)
def update_hospital(hospital_id: int, hospital_data: HospitalCreate):
    hospital_service = HospitalService()
    return hospital_service.update_hospital(hospital_id, hospital_data)


@router.delete("/hospital/{hospital_id}", response_model=GetHospitalResponse)
def delete_hospital(hospital_id: int):
    hospital_service = HospitalService()
    try:
        return hospital_service.delete_hospital(hospital_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
