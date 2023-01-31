from datetime import datetime
from typing import Optional
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


class TransactionSchema(BaseSchema):
    uuid: str
    patient: PatientSchema
    pharmacy: PharmacySchema
    amount: float
    timestamp: datetime


class PharmacyParametersApiSchema(BaseSchema):
    pharmacy_id: Optional[str]
    name: Optional[str]
    city: Optional[str]


class PatientParametersApiSchema(BaseSchema):
    patient_id: Optional[str]
    first_name: Optional[str]


class TransactionParametersApiSchema(BaseSchema):
    transaction_id: Optional[str]
    patient_id: Optional[str]
    pharmacy_id: Optional[str]
