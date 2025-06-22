from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import numpy as np
from schemas import PrediccionInput
from mappings.codificadores import mapa_sector_inverso, sector_a_zona, mapa_zona_inverso, mapa_grupo_incidente
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Prediccion de incidentes")

frontend_url = os.getenv("FRONTEND_URL")  # Valor por defecto si no existe

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],
    allow_credentials=True,
    allow_methods=["POST", "GET"], 
    allow_headers=["Content-Type"],
)

modelo_nn = load_model("model/modelo_nn_optimo.keras")

categorical_cols = ['turno_cod', 'sector_cod', 'zona_cod', 'dia_semana_cod']
numeric_cols = ['año', 'mes', 'día', 'es_fin_semana']

def transformar_input_real(data: PrediccionInput):
    dias_traducidos = {
        'Lunes': 0, 'Martes': 1, 'Miércoles': 2,
        'Jueves': 3, 'Viernes': 4, 'Sábado': 5, 'Domingo': 6
    }
    orden_turno = {'Mañana': 1, 'Tarde': 2, 'Noche': 3}

    try:
        dia_cod = dias_traducidos[data.nombre_dia]
        es_fin_semana = 1 if dia_cod in [5, 6] else 0
        turno_cod = orden_turno[data.turno]
        sector_cod = mapa_sector_inverso[data.sector_nombre]
        zona_nombre = sector_a_zona[data.sector_nombre]
        zona_cod = mapa_zona_inverso[zona_nombre]
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Valor inválido: {e}")

    return {
        'año': data.año,
        'mes': data.mes,
        'día': data.día,
        'dia_semana_cod': dia_cod,
        'es_fin_semana': es_fin_semana,
        'turno_cod': turno_cod,
        'sector_cod': sector_cod,
        'zona_cod': zona_cod
    }

@app.get("/")
async def root():
    return { "message": "Hello world" }

@app.post("/predict", summary="Predice el Top-5 de incidencias más probables")
def predicion(data: PrediccionInput):
    entrada = transformar_input_real(data)

    entrada_cat = [np.array([entrada[col]]) for col in categorical_cols]
    entrada_num = np.array([[entrada[col] for col in numeric_cols]])

    test = modelo_nn.predict(entrada_cat + [entrada_num], verbose=0)[0]
    top5_idx = np.argsort(test)[::-1][:5]

    results = []
    for idx in top5_idx:
        grupo_nombre = mapa_grupo_incidente.get(idx)
        if grupo_nombre is None:
            raise HTTPException(status_code=500, detail=f"Grupo {idx} no tiene nombre asignado.")
        
        results.append({
            "grupo": grupo_nombre,
            "probabilidad": float(test[idx])
        })

    return {"top_5": results}