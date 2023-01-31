from typing import Optional

from sqlalchemy import or_, select
from sqlalchemy.orm.decl_api import DeclarativeMeta

from models import engine, session
from models.database import Patients, Pharmacies, Transactions
from schemas.financial import *


class FinancialController:
    def __init__(self, table: Optional[DeclarativeMeta] = None) -> None:
        self.table = table

    async def query(self, parameters=None) -> list:
        if isinstance(parameters, PharmacyParametersApiSchema):
            return await self.__query_parameters_pharmacy(parameters)
        elif isinstance(parameters, PatientParametersApiSchema):
            return await self.__query_parameters_patient(parameters)
        return await self.__select_all()

    async def __query_parameters_pharmacy(
        self, parameters: PharmacyParametersApiSchema
    ) -> list[Optional[PharmacySchema]]:
        async with session() as s:
            query = await s.execute(
                select(self.table).where(
                    or_(
                        self.table.uuid == parameters.pharmacy_id,
                        self.table.name == parameters.name,
                        self.table.city == parameters.city,
                    )
                )
            )

            await engine.dispose()

            results = query.scalars().all()

            return [result.__dict__ for result in results]

    async def __query_parameters_patient(
        self, parameters: PatientParametersApiSchema
    ) -> list[Optional[PatientSchema]]:
        async with session() as s:
            query = await s.execute(
                select(self.table).where(
                    or_(
                        self.table.uuid == parameters.patient_id,
                        self.table.first_name == parameters.first_name,
                    )
                )
            )

            await engine.dispose()

            results = query.scalars().all()

            return [result.__dict__ for result in results]

    async def __select_all(self) -> list:
        async with session() as s:
            query = await s.execute(select(self.table))

            await engine.dispose()

            results = query.scalars().all()

            return [result.__dict__ for result in results]

    async def query_transaction(
        self, parameter: Optional[TransactionParametersApiSchema] = None
    ) -> list:
        if parameter:
            return await self.__query_parameters_transaction(parameter)
        return await self.__select_all_transaction()

    async def __query_parameters_transaction(
        self, parameters: TransactionParametersApiSchema
    ) -> list[Optional[TransactionSchema]]:
        async with session() as s:
            query = await s.execute(
                select(Transactions, Patients, Pharmacies)
                .join(Transactions.patient)
                .join(Transactions.pharmacy)
                .where(
                    or_(
                        Transactions.uuid == parameters.transaction_id,
                        Transactions.patient_uuid == parameters.patient_id,
                        Transactions.pharmacy_uuid == parameters.pharmacy_id,
                    )
                )
            )

            await engine.dispose()

            results = query.all()

            return [TransactionSchema.from_orm(result[0]) for result in results]

    async def __select_all_transaction(self) -> list[TransactionSchema]:
        async with session() as s:
            query = await s.execute(
                select(Transactions, Patients, Pharmacies)
                .join(Transactions.patient)
                .join(Transactions.pharmacy)
            )
            await engine.dispose()

            results = query.all()

            return [TransactionSchema.from_orm(result[0]) for result in results]
