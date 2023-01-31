# TODO: Criar o mock do sqlachemy usando o sqlite.
import pytest

from controllers.auth import AuthController
from main import app
from schemas.users import UserSchema


def mock_scan_token() -> list:
    return UserSchema(username="TestUsername", password="Test123")


@pytest.fixture
def authenticate() -> None:
    app.dependency_overrides[AuthController.scan_token] = mock_scan_token
    yield
    app.dependency_overrides = {}
