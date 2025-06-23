from fastapi import APIRouter, status
from app.schemas.feedback import FeedbackPayload
from datetime import datetime
import json
import os

router = APIRouter()

FEEDBACK_FILE = "feedbacks_tmp.json"

@router.post("/feedback", status_code=status.HTTP_201_CREATED)
def recibir_feedback(feedback: FeedbackPayload):
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w") as f:
            json.dump([], f)

    with open(FEEDBACK_FILE, "r+") as f:
        data = json.load(f)
        data.append(feedback.dict())
        f.seek(0)
        json.dump(data, f, indent=2)

    return {"message": "Feedback guardado temporalmente"}