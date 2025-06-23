from pydantic import BaseModel
from typing import List, Literal

class InputData(BaseModel):
    fecha: str
    turno: str
    sector: str

class FeedbackPayload(BaseModel):
    timestamp: str
    input_data: InputData
    predicted: List[str]
    feedback: Literal["Coincide", "No coincide"]
    actual_incident: List[str]