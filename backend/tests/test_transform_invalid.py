import pytest
from app.dependencies.transform_input import transformar_input_real
from app.schemas.prediccion_input import PrediccionInput
from fastapi import HTTPException

def test_transformar_input_dia_invalido():
    with pytest.raises(HTTPException):
        transformar_input_real(PrediccionInput(
            año=2025,
            mes=6,
            día=21,
            nombre_dia="Blursday",
            turno="Mañana",
            sector_nombre="El Recreo"
        ))

def test_transformar_input_turno_invalido():
    with pytest.raises(HTTPException):
        transformar_input_real(PrediccionInput(
            año=2025,
            mes=6,
            día=21,
            nombre_dia="Sábado",
            turno="Madrugada",
            sector_nombre="El Recreo"
        ))

def test_transformar_input_sector_invalido():
    with pytest.raises(HTTPException):
        transformar_input_real(PrediccionInput(
            año=2025,
            mes=6,
            día=21,
            nombre_dia="Sábado",
            turno="Noche",
            sector_nombre="Sector Falso"
        ))
