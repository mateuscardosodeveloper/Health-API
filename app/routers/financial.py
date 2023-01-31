from typing import Optional

from fastapi import APIRouter, Depends, Path, Query

from controllers.auth import AuthController
from controllers.financial import FinancialController
from models.database import Patients, Pharmacies
from schemas.financial import *

router = APIRouter()


@router.get(
    "/patients",
    summary="Query patients",
    response_model=list[PatientSchema],
    dependencies=[Depends(AuthController.scan_token)],
)
async def patient_all(
    patient_id: Optional[str] = Query(None), first_name: Optional[str] = Query(None)
):
    filters = None

    if patient_id or first_name:
        filters = PatientParametersApiSchema(
            patient_id=patient_id, first_name=first_name
        )

    return await FinancialController(table=Patients).query(parameters=filters)


@router.get(
    "/pharmacies",
    summary="Query pharmacies",
    response_model=list[PharmacySchema],
    dependencies=[Depends(AuthController.scan_token)],
)
async def pharmacy_all(
    pharmacy_id: Optional[str] = Query(None),
    name: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
):

    filters = None

    if pharmacy_id or name or city:
        filters = PharmacyParametersApiSchema(
            pharmacy_id=pharmacy_id, name=name, city=city
        )

    return await FinancialController(table=Pharmacies).query(parameters=filters)


@router.get(
    "/transactions",
    summary="Query transactions",
    response_model=list[TransactionSchema],
    dependencies=[Depends(AuthController.scan_token)],
)
async def pharmacy_all(
    transaction_id: Optional[str] = Query(None),
    patient_id: Optional[str] = Query(None),
    pharmacy_id: Optional[str] = Query(None),
):
    filters = None

    if transaction_id or patient_id or pharmacy_id:
        filters = TransactionParametersApiSchema(
            transaction_id=transaction_id,
            patient_id=patient_id,
            pharmacy_id=pharmacy_id,
        )

    return await FinancialController().query_transaction(parameter=filters)
