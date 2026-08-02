from pydantic_settings import BaseSettings
from datetime import timedelta

class Settings(BaseSettings):
    APP_NAME: str = "AI Factory Safety Copilot"

    VERSION: str = "1.0"

    SECRET_KEY: str = "factory-secret-key"

    DATABASE_URL: str = "sqlite:///factory.db"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()