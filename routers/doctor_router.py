from fastapi import APIRouter, HTTPException
from schemas.doctor import Doctor, DoctorCreate
from typing import List
from database import doctors_db

doctor_routers = APIRouter()

@doctor_routers.post("/doctors/", response_model=Doctor)
def create_doctor(doctor_create: DoctorCreate):
    doctor = Doctor(id=len(doctors_db) + 1,
                    name=doctor_create.name,
                    specialization=doctor_create.specialization,
                    phone=doctor_create.phone,
                    is_available=True)
    doctors_db.append(doctor)
    return doctor

@doctor_routers.get("/doctors/", response_model=List[Doctor])
def read_doctors():
    return doctors_db


@doctor_routers.get("/doctors/{doctor_id}", response_model=Doctor)
def read_doctor(doctor_id: int):
    doctor = next((d for d in doctors_db if d.id == doctor_id), None)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor
