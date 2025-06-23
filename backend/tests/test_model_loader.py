import pytest
from app.ml.model_loader import modelo_nn

def test_model_cargado():
    assert modelo_nn is not None
    assert hasattr(modelo_nn, "predict")
