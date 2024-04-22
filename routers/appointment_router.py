from fastapi import APIRouter, HTTPException
from schemas.appointment import Appointment
from typing import List
from database import patients_db, appointments_db, doctors_db

appointment_routers = APIRouter()

@appointment_routers.post("/appointments/", response_model=Appointment)
def create_appointment(patient_id: int, date: str):
    # Check if patient exists
    patient = next((p for p in patients_db if p.id == patient_id), None)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Find the first available doctor
    doctor = next((d for d in doctors_db if d.is_available), None)
    if not doctor:
        raise HTTPException(status_code=404, detail="No available doctors")

    appointment = Appointment(id=len(appointments_db) + 1, patient_id=patient_id, doctor_id=doctor.id, date=date)
    appointments_db.append(appointment)

    # Set doctor's availability to False
    doctor.is_available = False

    return appointment

# Endpoint to complete an appointment
@appointment_routers.put("/appointments/{appointment_id}/complete/")
def complete_appointment(appointment_id: int):
    appointment = next((a for a in appointments_db if a.id == appointment_id), None)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    doctor = next((d for d in doctors_db if d.id == appointment.doctor_id), None)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor.is_available = True
    appointments_db.remove(appointment)

    return {"message": "Appointment completed successfully"}

# Endpoint to cancel an appointment
@appointment_routers.delete("/appointments/{appointment_id}/cancel/")
def cancel_appointment(appointment_id: int):
    appointment = next((a for a in appointments_db if a.id == appointment_id), None)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    doctor = next((d for d in doctors_db if d.id == appointment.doctor_id), None)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    doctor.is_available = True
    appointments_db.remove(appointment)

    return {"message": "Appointment canceled successfully"}

