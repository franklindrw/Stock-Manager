from pydantic_settings import BaseSettings, SettingsConfigDict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int = 5432
    POSTGRES_DB: str

    @property
    def db_url(self) -> str:
        return f"postgresql+psycopg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

class DBConnection:
    __engine = None

    def __init__(self) -> None:
        if DBConnection.__engine is None:
            settings = Settings()
            DBConnection.__engine = create_engine(
                settings.db_url,
                pool_size=10,
                pool_pre_ping=True,
                max_overflow=20,
                pool_timeout=30,
                pool_recycle=1800
            )

        self.session_maker = sessionmaker(
            bind=DBConnection.__engine,
            autocommit=False,
            autoflush=False
        )
        self.session = None

    def __enter__(self):
        self.session = self.session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()
