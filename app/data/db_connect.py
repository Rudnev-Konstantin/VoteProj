from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Declarative_Base = declarative_base()


class DataBaseConnect:
    def __init__(self, db_url: str, create_tables=True, fill_default_data=True):
        if not db_url or not db_url.strip():
            raise ValueError("URL базы данных не может быть пустым")
        
        from .models import __all_models__
        
        self.engine = create_engine(db_url)
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
        )
        
        if create_tables:
            self.create_tables()
            if fill_default_data:
                self.fill_default_data()
    
    def create_tables(self):
        Declarative_Base.metadata.create_all(self.engine)
    
    def fill_default_data(self):
        from default_data import fill_all_default_data
        fill_all_default_data(self.get_session())
    
    def get_session(self):
        return self.SessionLocal()
