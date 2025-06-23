import requests
import numpy as np
from app.mappings.codificadores import mapa_grupo_incidente
from app.core.config import get_settings

settings = get_settings()
TFSERVING_URL = f"{settings.ML_URL}/v1/models/1:predict"

categorical_cols = ['turno_cod', 'sector_cod', 'zona_cod', 'dia_semana_cod']
numeric_cols = ['año', 'mes', 'día', 'es_fin_semana']

def predecir_top_5(entrada: dict):
    # Reestructuramos el input
    payload = {
        "signature_name": "serving_default",
        "inputs": {
            "turno_cod_input": [[entrada['turno_cod']]],
            "sector_cod_input": [[entrada['sector_cod']]],
            "zona_cod_input": [[entrada['zona_cod']]],
            "dia_semana_cod_input": [[entrada['dia_semana_cod']]],
            "numerical_input": [[
                entrada['año'],
                entrada['mes'],
                entrada['día'],
                entrada['es_fin_semana']
            ]]
        }
    }

    response = requests.post(TFSERVING_URL, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Error al consultar el modelo: {response.text}")

    prediction = response.json()['outputs']  # matriz (1,14)

    # Obtener los índices de las 5 clases más probables
    prediction_array = np.array(prediction)[0]
    top_5_indices = prediction_array.argsort()[-5:][::-1]
    top_5_prob = prediction_array[top_5_indices]

    # Mapear a nombres si ya tienes un diccionario
    from app.mappings.codificadores import mapa_grupo_incidente
    top_5_result = [
        {
            "grupo_incidente": mapa_grupo_incidente[idx],
            "probabilidad": float(prob)
        }
        for idx, prob in zip(top_5_indices, top_5_prob)
    ]

    return top_5_result