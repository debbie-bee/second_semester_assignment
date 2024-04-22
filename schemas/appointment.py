from pydantic import BaseModel
from typing import Optional
from .patient import Patient
from .doctor import Doctor

class Appointment(BaseModel):
    id: int
    patient: Patient
    doctor: Doctor
    date: str