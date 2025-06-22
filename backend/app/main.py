from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes_predict import router as predict_router
from app.core.config import get_settings

app = FastAPI(title="Predicción de Incidentes")

settings = get_settings()
print("ORIGINS:", settings.FRONTEND_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.FRONTEND_URL,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(predict_router, tags=["Prediccion"])
