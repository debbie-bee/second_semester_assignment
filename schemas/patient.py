from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str

class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str