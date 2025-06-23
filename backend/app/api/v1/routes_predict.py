import logging
import time
import json
from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.schemas.prediccion_input import PrediccionInput
from app.dependencies.transform_input import transformar_input_real
from app.ml.predictor import predecir_top_5
import os

# os.makedirs("logs", exist_ok=True)

# log_filename = f"logs/prediction-{datetime.now().strftime('%Y-%m-%d')}.log"

# logger = logging.getLogger("prediction_logger")
# logger.setLevel(logging.INFO)

# handler = logging.FileHandler(log_filename)
# formatter = logging.Formatter(
#     '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}'
# )
# handler.setFormatter(formatter)
# logger.addHandler(handler)

router = APIRouter()

@router.post("/predict")
def prediccion(data: PrediccionInput):
    entrada = transformar_input_real(data)
    # start_time = time.time()

    try:
        resultado = predecir_top_5(entrada)
        # latency = round(time.time() - start_time, 3)

        # logger.info(json.dumps({
        #     "endpoint": "/predict",
        #     "input": entrada,
        #     "output": resultado,
        #     "latency": latency
        # }))

        return {"top_5": resultado}
    except Exception as e:
        # logger.error(json.dumps({
        #     "endpoint": "/predict",
        #     "input": entrada,
        #     "error": str(e)
        # }))
        raise HTTPException(status_code=500, detail=str(e))
    