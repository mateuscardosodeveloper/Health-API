from typing import Optional, Protocol
from sqlalchemy import select
from fastapi import HTTPException

from models.database import Transactions, Pharmacies, Patients
from schemas.financial import Transaction
from models import session, engine


class TablesSqlite(Protocol):
    def patients() -> Patients:
        ...

    def pharmacies() -> Pharmacies:
        ...

    def transactions() -> Transactions:
        ...


class FinancialController:

    def __init__(self, table: Optional[TablesSqlite] = None) -> None:
        self.table = table

    async def select_all(self) -> list:
        async with session() as s:
            query = await s.execute(select(self.table))

            await engine.dispose()

            results = query.scalars().all()

            return [result.__dict__ for result in results]

    async def query_transaction(self) -> list[Transaction]:
        async with session() as s:
            query = await s.execute(
                select(Transactions, Patients, Pharmacies).join(Transactions.patient).join(Transactions.pharmacy))
            await engine.dispose()

            results = query.all()

            return [Transaction.from_orm(result[0]) for result in results]
