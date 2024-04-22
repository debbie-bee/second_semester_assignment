from pydantic import BaseModel
from typing import Optional


class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: Optional[bool] = True

class  DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: str