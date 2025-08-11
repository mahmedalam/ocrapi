from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the backend."""

    API_PREFIX: str
    API_KEY: str
    DEBUG: bool
    MISTRAL_MODEL: str
    MISTRAL_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
