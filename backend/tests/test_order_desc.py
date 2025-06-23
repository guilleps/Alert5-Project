import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_orden_descendente_probabilidades():
    payload = {
        "año": 2025,
        "mes": 6,
        "día": 21,
        "nombre_dia": "Domingo",
        "turno": "Tarde",
        "sector_nombre": "El Recreo"
    }

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/predict", json=payload)
        assert response.status_code == 200
        top_5 = response.json()["top_5"]
        probabilidades = [r["probabilidad"] for r in top_5]
        assert probabilidades == sorted(probabilidades, reverse=True)
