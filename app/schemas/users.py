from datetime import datetime
from typing import Union

from passlib.hash import bcrypt

from schemas import BaseSchema


class UserSchema(BaseSchema):
    username: str
    password: str

    def encrypt_password(self) -> None:
        self.password = bcrypt.hash(self.password)


class AuthTokenSchema(BaseSchema):
    access_token: str
    expires_in: Union[str, datetime]
    token_type: str = "Bearer"
