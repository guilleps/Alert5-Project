from typing import List
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    FRONTEND_URL: List[str] = ["http://localhost:5173"]
    ML_URL: str = "http://localhost:8501"
    MODEL_ML: str = "http://localhost:8502"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()