from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .settings import Settings

settings = Settings()

class DBConnection:
    __engine = None

    def __init__(self) -> None:
        if DBConnection.__engine is None:
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
            autocommit=False, # evita commits automaticos
            autoflush=False # evita concorrencia de sessoes
        )
        self.session = None

    def __enter__(self):
        self.session = self.session_maker()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()