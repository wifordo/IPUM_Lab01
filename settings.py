from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    # Dodajemy pole na sekret
    SUPER_SECRET_KEY: str

    # Konfiguracja odczytu z pliku .env.dev (domyślnie)
    model_config = SettingsConfigDict()

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value: str) -> str:
        allowed = ["dev", "test", "prod"]
        if value not in allowed:
            raise ValueError(f"ENVIRONMENT must be one of: {', '.join(allowed)}")
        return value
