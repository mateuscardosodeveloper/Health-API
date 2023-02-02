import pytest
from fastapi import HTTPException

from controllers.auth import AuthController
from controllers.user import UserController
from schemas.users import AuthTokenSchema, UserSchema


@pytest.mark.asyncio
async def test_create_user_successfully(mock_create_user, faker) -> None:
    user = UserSchema(username=faker.pystr(), password=faker.pystr())
    response = await UserController.create(user)

    assert response.status_code == 201
    assert response.body == b'{"message":"User created successfully."}'
    assert mock_create_user.called is True
    assert mock_create_user.call_count is 1


@pytest.mark.asyncio
async def test_create_user_failed(mock_create_user_fail, faker) -> None:
    with pytest.raises(HTTPException):
        user = UserSchema(username=faker.pystr(), password=faker.pystr())
        response = await UserController.create(user)

        assert response.status_code is 403
        assert response.detail is "Username already exists."
        assert mock_create_user_fail.called is True
        assert mock_create_user_fail.call_count is 1


@pytest.mark.asyncio
async def test_authenticate_successfully(mock_login) -> None:
    user = UserSchema(username="Tester", password="123")
    response = await AuthController.authenticate(
        credentials=user, method=UserController
    )

    assert isinstance(response, AuthTokenSchema)
    assert mock_login.called is True
    assert mock_login.call_count is 1


@pytest.mark.asyncio
async def test_authenticate_incorrect_password(mock_login) -> None:
    with pytest.raises(HTTPException):
        user = UserSchema(username="Tester", password="1234")
        response = await AuthController.authenticate(
            credentials=user, method=UserController
        )

        assert response.status_code is 400
        assert response.detail is "Wrong password."
        assert mock_login.called is True
        assert mock_login.call_count is 1


@pytest.mark.asyncio
async def test_authenticate_incorrect_username(mock_login_fail, faker) -> None:
    with pytest.raises(HTTPException):
        user = UserSchema(username=faker.pystr(), password=faker.pystr())
        response = await AuthController.authenticate(
            credentials=user, method=UserController
        )

        assert response.status_code is 400
        assert response.detail is "Username doesn't not exists."
        assert mock_login_fail.called is True
        assert mock_login_fail.call_count is 1
