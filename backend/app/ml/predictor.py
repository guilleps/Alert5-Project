import numpy as np
from app.ml.model_loader import modelo_nn
from app.mappings.codificadores import mapa_grupo_incidente

categorical_cols = ['turno_cod', 'sector_cod', 'zona_cod', 'dia_semana_cod']
numeric_cols = ['año', 'mes', 'día', 'es_fin_semana']

def predecir_top_5(entrada: dict):
    entrada_cat = [np.array([entrada[col]]) for col in categorical_cols]
    entrada_num = np.array([[entrada[col] for col in numeric_cols]])

    test = modelo_nn.predict(entrada_cat + [entrada_num], verbose=0)[0]
    top5_idx = np.argsort(test)[::-1][:5]

    results = []
    for idx in top5_idx:
        grupo_nombre = mapa_grupo_incidente.get(idx)
        if grupo_nombre is None:
            raise ValueError(f"Grupo {idx} no tiene nombre asignado.")
        results.append({"grupo": grupo_nombre, "probabilidad": float(test[idx])})
    return results
