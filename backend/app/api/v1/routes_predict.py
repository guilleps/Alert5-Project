from fastapi import APIRouter, HTTPException
from app.schemas.prediccion_input import PrediccionInput
from app.dependencies.transform_input import transformar_input_real
from app.ml.predictor import predecir_top_5

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/predict")
def prediccion(data: PrediccionInput):
    entrada = transformar_input_real(data)
    try:
        resultado = predecir_top_5(entrada)
        return {"top_5": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
