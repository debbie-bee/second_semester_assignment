from fastapi import APIRouter, HTTPException
from schemas.patient import Patient, PatientCreate
from typing import List
from database import patients_db, Patient

patient_routers = APIRouter()


# CRUD endpoints for Patients
@patient_routers.post("/patients/", response_model=Patient)
def create_patient(patient_create: PatientCreate):
    patient= Patient(id=len(patients_db) + 1,
                     name=patient_create.name,
                     age=patient_create.age,
                     sex=patient_create.sex,
                     weight=patient_create.weight,
                     height=patient_create.height,
                     phone=patient_create.phone,
    )
    patients_db.append(patient)
    return patient

@patient_routers.get("/patients/", response_model=List[Patient])
def read_patients():
    return patients_db 

@patient_routers.get("/patients/{patient_id}", response_model=Patient)
def read_patient(patient_id: int):
    patient = next((p for p in patients_db if p.id == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
