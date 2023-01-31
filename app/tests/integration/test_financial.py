import pytest
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_get_patients_successfully(authenticate) -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/health/patients")

    assert response.status_code is 200
    assert isinstance(response.json(), list)
    assert isinstance(response.json()[0], dict)


@pytest.mark.asyncio
async def test_get_patients_query_parameters_successfully(authenticate) -> None:
    filters = {"patient_id": "PATIENT0001", "first_name": "GUSTAVO"}

    for key, value in filters.items():
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/api/health/patients", params={key: value})

        assert response.status_code is 200
        assert isinstance(response.json()[0], dict)


@pytest.mark.asyncio
async def test_get_patientes_without_authentication() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/health/patients")

    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}


@pytest.mark.asyncio
async def test_get_pharmacies_successfully(authenticate) -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/health/pharmacies")

    assert response.status_code is 200
    assert isinstance(response.json(), list)
    assert isinstance(response.json()[0], dict)


@pytest.mark.asyncio
async def test_get_pharmacies_query_parameters_successfully(authenticate) -> None:
    filters = {"city": "CAMPINAS", "name": "DROGAO SUPER", "pharmacy_id": "PHARM0010"}

    for key, value in filters.items():
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/api/health/pharmacies", params={key: value})

        assert response.status_code is 200
        assert isinstance(response.json()[0], dict)


@pytest.mark.asyncio
async def test_get_pharmacies_without_authentication() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/health/pharmacies")

    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}


@pytest.mark.asyncio
async def test_get_transactions_successfully(authenticate) -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/health/transactions")

    assert response.status_code is 200
    assert isinstance(response.json(), list)
    assert isinstance(response.json()[0], dict)


@pytest.mark.asyncio
async def test_get_transactions_query_parameters_successfully(authenticate) -> None:
    filters = {
        "transaction_id": "TRAN0001",
        "patient_id": "PATIENT0045",
        "pharmacy_id": "PHARM0001",
    }

    for key, value in filters.items():
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/api/health/transactions", params={key: value})

        assert response.status_code is 200
        assert isinstance(response.json()[0], dict)


@pytest.mark.asyncio
async def test_get_transactions_without_authentication() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/health/transactions")

    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}
