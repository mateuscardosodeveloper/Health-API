from datetime import datetime
from schemas import BaseSchema


class PharmacySchema(BaseSchema):
    uuid: str
    name: str
    city: str


class PatientSchema(BaseSchema):
    uuid: str
    first_name: str
    last_name: str
    date_of_birth: datetime


class Transaction(BaseSchema):
    uuid: str
    patient: PatientSchema
    pharmacy: PharmacySchema
    amount: float
    timestamp: datetime
