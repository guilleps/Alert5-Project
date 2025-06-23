import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_predict_success():
    payload = {
        "año": 2025,
        "mes": 6,
        "día": 14,
        "nombre_dia": "Viernes",
        "turno": "Tarde",
        "sector_nombre": "Sto.Dominguito"
    }

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/predict", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "top_5" in data
        assert isinstance(data["top_5"], list)
        assert len(data["top_5"]) == 5

@pytest.mark.asyncio
async def test_predict_invalid_input():
    payload = {
        "año": 2025,
        "mes": 13,
        "día": 14,
        "nombre_dia": "Neptuno",
        "turno": "Tarde",
        "sector_nombre": "Sector Inexistente"
    }

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/predict", json=payload)
        assert response.status_code == 422 or response.status_code == 400
