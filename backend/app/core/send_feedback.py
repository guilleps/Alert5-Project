import requests
import json
import os
from app.core.config import get_settings

FEEDBACK_FILE = "feedbacks_tmp.json"

settings = get_settings()
MODEL_ML = f"{settings.MODEL_ML}/v1/models/1:feedback"

def send_feedback_today():
    if not os.path.exists(FEEDBACK_FILE):
        print("No hay feedbacks para enviar.")
        return

    with open(FEEDBACK_FILE, "r") as f:
        data = json.load(f)

    if not data:
        print("Archivo vacío.")
        return

    # Enviar a endpoint final
    response = requests.post(MODEL_ML, json={"feedbacks": data})
    if response.status_code == 200:
        print("Feedbacks enviados correctamente.")
        # Borrar archivo temporal
        os.remove(FEEDBACK_FILE)
    else:
        print("Error al enviar feedbacks:", response.text)