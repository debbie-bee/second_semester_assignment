from fastapi import FastAPI
from typing import List

from schemas.doctor import Doctor
from schemas.patient import Patient
from schemas.appointment import Appointment

from routers.patient_router import patient_routers
from routers.doctor_router import doctor_routers
from routers.appointment_router import appointment_routers 

app = FastAPI()


app.include_router(patient_routers, prefix="/patients", tags=["Patients"])
app.include_router(doctor_routers, prefix="/doctors", tags=["Doctors"])
app.include_router(appointment_routers, prefix="/appointments", tags=["Appointments"])

                   
@app.get("/")
def home():
    return "Welcome to my Assignment"