import pytest
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import delete

from controllers.auth import AuthController
from controllers.user import UserController
from main import app
from models import session
from models.database import Users
from schemas.users import UserSchema


async def remove_user() -> None:
    async with session() as se:
        await se.execute(delete(Users).where(Users.username == "Test"))
        await se.commit()


def mock_scan_token() -> list:
    return UserSchema(username="TestUsername", password="Test123")


@pytest.fixture
def authenticate() -> None:
    app.dependency_overrides[AuthController.scan_token] = mock_scan_token
    yield
    app.dependency_overrides = {}


@pytest.fixture
def mock_create_user(mocker) -> None:
    yield mocker.patch.object(
        UserController,
        "_UserController__inser_user",
        return_value=JSONResponse(
            status_code=201, content={"message": "User created successfully."}
        ),
    )


@pytest.fixture
def mock_create_user_fail(mocker) -> None:
    yield mocker.patch.object(
        UserController,
        "_UserController__inser_user",
        side_effect=HTTPException(detail="Username already exists.", status_code=403),
    )


@pytest.fixture
def mock_login(mocker) -> None:
    from uuid import uuid4

    user = UserSchema(
        username="Tester",
        password="$2b$12$VJzLD55y//LC8/5jWGJ3L.rufs7nuiVQDcweIoX1N8cOUBh5QHiim",
    )
    user.uuid = str(uuid4())

    yield mocker.patch.object(UserController, "login", return_value=user)


@pytest.fixture
def mock_login_fail(mocker) -> None:
    yield mocker.patch.object(
        UserController,
        "login",
        side_effect=HTTPException(
            status_code=400, detail="Username doesn't not exists."
        ),
    )
