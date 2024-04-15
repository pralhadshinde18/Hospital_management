from fastapi import APIRouter, HTTPException
from schema.technician_schema import TechnicianBase, TechnicianCreate, GetTechnicianResponse
from service.technician_service import TechnicianService
from typing import List

router = APIRouter()


@router.post("/technician/", response_model=TechnicianBase)
def create_technician(technician_data: TechnicianCreate):
    technician_service = TechnicianService()
    return technician_service.create_technician(technician_data)


@router.get("/technician/", response_model=List[GetTechnicianResponse])
def get_all_technician():
    technician_service = TechnicianService()
    return technician_service.get_all_technician()


@router.put("/technician/{technician_id}", response_model=TechnicianBase)
def update_technician(technician_id: int, technician_data: TechnicianCreate):
    technician_service = TechnicianService()
    return technician_service.update_technician(technician_id, technician_data)


@router.delete("/technician/{technician_id}", response_model=GetTechnicianResponse)
def delete_technician(technician_id: int):
    technician_service = TechnicianService()
    try:
        return technician_service.delete_technician(technician_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
