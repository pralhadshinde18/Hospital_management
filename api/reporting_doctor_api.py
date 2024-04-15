from fastapi import APIRouter, HTTPException
from service.reporting_doctor_service import ReportingDoctorService
from schema.reporting_doctor_schema import ReportingDoctorBase, GetReportingDoctor, ReportingDoctorCreate
from typing import List

router = APIRouter()


@router.post("/reporting_doctor/", response_model=ReportingDoctorBase)
def create_reporting_doctor(reporting_doctor_data: ReportingDoctorCreate):
    reporting_doctor_service = ReportingDoctorService()
    return reporting_doctor_service.create_reporting_doctor(reporting_doctor_data)


@router.get("/reporting_doctor/", response_model=List[GetReportingDoctor])
def get_reporting_doctor():
    reporting_doctor_service = ReportingDoctorService()
    return reporting_doctor_service.get_reporting_doctor()


@router.put("/reporting_doctor/{reporting_doctor_id}", response_model=ReportingDoctorBase)
def update_reporting_doctor(reporting_doctor_id: int, reporting_doctor_data: ReportingDoctorCreate):
    reporting_doctor_service = ReportingDoctorService()
    return reporting_doctor_service.update_reporting_doctor(reporting_doctor_id, reporting_doctor_data)


@router.delete("/reporting_doctor/{reporting_doctor_id}", response_model=GetReportingDoctor)
def deelete_reporting_doctor(reporting_doctor_id: int):
    reporting_doctor_service = ReportingDoctorService()
    try:
        return reporting_doctor_service.delete_reporting_doctor(reporting_doctor_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
