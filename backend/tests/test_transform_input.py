import pytest
from app.dependencies.transform_input import transformar_input_real
from app.schemas.prediccion_input import PrediccionInput

def test_transformar_input_real_valido():
    data = PrediccionInput(
        año=2025,
        mes=6,
        día=21,
        nombre_dia="Sábado",
        turno="Noche",
        sector_nombre="El Recreo"
    )
    resultado = transformar_input_real(data)
    assert resultado["dia_semana_cod"] == 5
    assert resultado["es_fin_semana"] == 1
    assert resultado["turno_cod"] == 3
    assert resultado["sector_cod"] >= 0
    assert resultado["zona_cod"] >= 0
