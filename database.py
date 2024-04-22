from typing import List
from schemas.doctor import Doctor
from schemas.patient import Patient
from schemas.appointment import Appointment


patients_db: List[Patient] = []
doctors_db: List[Doctor] = []
appointments_db: List[Appointment] = []