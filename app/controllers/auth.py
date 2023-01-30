
import jwt
from typing import Protocol
from passlib.hash import bcrypt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, Request, HTTPException

from settings import settings
from models.database import Users
from schemas.users import AuthTokenSchema, UserSchema


class CustomOAuth2PwdBearer(OAuth2PasswordBearer):

    async def __call__(self, request: Request):
        authorization: str = request.headers.get("Authorization")

        if not authorization:
            raise HTTPException(status_code=401, headers={"WWW-Authenticate": "JWT/Bearer"})

        scheme, _, param = authorization.partition(" ")

        if scheme.lower() not in ["jwt", "bearer"]:
            raise HTTPException(status_code=401, headers={"WWW-Authenticate": "JWT/Bearer"})

        return param


oauth_scheme = CustomOAuth2PwdBearer(tokenUrl="/api/health/authentication")


class UserControllerMethod(Protocol):
    @classmethod
    async def login(cls, username: str) -> Users:
        ...


class AuthController:
    @classmethod
    def create_token(cls, user: Users) -> None:
        expired_in = datetime.utcnow() + timedelta(
            hours=int(settings.EXPIRATION_TIME_HOUR)
        )

        data = {
            "id": user.uuid
        }

        cls.token = jwt.encode(data, settings.USER_PROJECT_KEY, algorithm="HS256")
        cls.expired_in = expired_in.isoformat()

    @classmethod
    def scan_token(cls, token: str = Depends(oauth_scheme)) -> None:
        try:
            jwt.decode(token, settings.USER_PROJECT_KEY, algorithms=["HS256"])

        except jwt.PyJWTError:
            raise HTTPException(status_code=401, detail="Invalid or expired token.")

    @classmethod
    async def authenticate(cls, credentials: UserSchema, method: UserControllerMethod) -> AuthTokenSchema:
        user = await method.login(username=credentials.username)

        if not bcrypt.verify(credentials.password, user.password):
            raise HTTPException(status_code=400, detail="Wrong password.")

        cls.create_token(user=user)

        return AuthTokenSchema(access_token=cls.token, expires_in=cls.expired_in)
