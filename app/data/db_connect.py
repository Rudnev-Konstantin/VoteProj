from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Declarative_Base = declarative_base()


class DataBaseConnect:
    def __init__(self, db_url: str):
        if not db_url or not db_url.strip():
            raise ValueError("URL базы данных не может быть пустым")
        
        self.engine = create_engine(db_url)
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
        )
    
    def get_session(self):
        return self.SessionLocal()
    
    def create_tables(self):
        from .models import __all_models__
        Declarative_Base.metadata.create_all(self.engine)
