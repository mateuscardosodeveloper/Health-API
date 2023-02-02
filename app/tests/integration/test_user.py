import pytest
from httpx import AsyncClient

from main import app
from schemas.users import AuthTokenSchema


@pytest.mark.asyncio
async def test_create_user_successfully() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            url="/api/health/user", json={"username": "Test", "password": "test123"}
        )

    assert response.status_code is 201
    assert response.json() == {"message": "User created successfully."}


@pytest.mark.asyncio
async def test_create_user_failed() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            url="/api/health/user", json={"username": "Test", "password": "test123"}
        )

    assert response.status_code == 403
    assert response.json() == {"detail": "Username already exists."}


@pytest.mark.asyncio
async def test_authentication_user_successfully() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            url="/api/health/authentication",
            data={"username": "Test", "password": "test123"},
        )

    assert response.status_code is 200
    assert response.json() == AuthTokenSchema(**response.json()).dict()


@pytest.mark.asyncio
async def test_authentication_user_wrong_username() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            url="/api/health/authentication",
            data={"username": "WrongUsername", "password": "test123"},
        )

    assert response.status_code == 400
    assert response.json() == {"detail": "Username doesn't not exists."}


@pytest.mark.asyncio
async def test_authentication_user_wrong_password() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            url="/api/health/authentication",
            data={"username": "Test", "password": "WrongPassword"},
        )

    assert response.status_code == 400
    assert response.json() == {"detail": "Wrong password."}


def teardown_module(module) -> None:
    import asyncio

    from tests.conftest import remove_user

    asyncio.run(remove_user())
