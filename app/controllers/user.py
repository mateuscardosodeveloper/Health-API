from uuid import uuid4

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import insert, select

from models import engine, session
from models.database import Users
from schemas.users import UserSchema
from utils.logging import error

# from sqlalchemy.engine.row import LegacyRow


class UserController:
    @classmethod
    async def login(cls, username: str) -> Users:
        async with session() as s:
            query = await s.execute(select(Users).where(Users.username == username))
            await engine.dispose()

            result = query.scalars().first()
            if result:
                return result

            raise HTTPException(status_code=400, detail="Username doesn't not exists.")

    @classmethod
    async def create(cls, user: UserSchema) -> JSONResponse:
        user.encrypt_password()
        data_insert = {
            "uuid": str(uuid4()),
            "username": user.username,
            "password": user.password,
        }
        return await cls.__inser_user(user=data_insert)

    @classmethod
    async def __inser_user(cls, user: dict) -> JSONResponse:
        async with session() as s:
            try:
                await s.execute(insert(Users).values(**user))
                await s.commit()
            except Exception as e:
                error(e)
                raise HTTPException(detail="Username already exists.", status_code=403)

            await engine.dispose()

        return JSONResponse(
            status_code=201, content={"message": "User created successfully."}
        )
