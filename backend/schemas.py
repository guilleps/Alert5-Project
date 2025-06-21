from pydantic import BaseModel

class PrediccionInput(BaseModel):
    año: int
    mes: int
    día: int
    nombre_dia: str
    turno: str
    sector_nombre: str