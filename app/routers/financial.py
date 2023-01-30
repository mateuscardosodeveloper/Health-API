from fastapi import APIRouter, Depends

from controllers.auth import AuthController
from controllers.financial import FinancialController
from schemas.financial import PatientSchema, PharmacySchema, Transaction
from models.database import Pharmacies, Patients


router = APIRouter()


@router.get(
    '/patients',
    summary='Query patients',
    response_model=list[PatientSchema],
    dependencies=[Depends(AuthController.scan_token)]
)
async def patient_all():
    return await FinancialController(table=Patients).select_all()


@router.get(
    '/pharmacies',
    summary='Query pharmacies',
    response_model=list[PharmacySchema],
    dependencies=[Depends(AuthController.scan_token)]
)
async def pharmacy_all():
    return await FinancialController(table=Pharmacies).select_all()


@router.get(
    '/transactions',
    summary='Query transactions',
    response_model=list[Transaction],
    dependencies=[Depends(AuthController.scan_token)]
)
async def pharmacy_all():
    return await FinancialController().query_transaction()
