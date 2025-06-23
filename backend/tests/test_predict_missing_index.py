import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_missing_index(monkeypatch):
    def dummy_predict(_):
        dummy_output = [0.0] * 30
        dummy_output[29] = 1.0
        return [dummy_output]

    # Parchar modelo
    from app.ml.model_loader import modelo_nn
    monkeypatch.setattr(modelo_nn, "predict", dummy_predict)

    payload = {
        "año": 2025,
        "mes": 6,
        "día": 21,
        "nombre_dia": "Sábado",
        "turno": "Tarde",
        "sector_nombre": "El Recreo"
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 500
