from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Tipagem clara e validação
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int = 5432
    POSTGRES_DB: str

    @property
    def db_url(self) -> str:
        # Gera a URL de conexão
        return f"postgresql+psycopg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()