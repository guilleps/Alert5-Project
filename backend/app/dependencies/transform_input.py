from app.mappings.codificadores import mapa_sector_inverso, sector_a_zona, mapa_zona_inverso
from app.schemas.prediccion_input import PrediccionInput
from fastapi import HTTPException

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
        raise HTTPException(
            status_code=400,
            detail=f"Entrada inválida en el campo: {str(e)}. Verifica que día, turno o sector sean correctos."
        )

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
