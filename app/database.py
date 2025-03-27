from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        self.sessionLocal  = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
    @contextmanager
    def getSession(self):
        session = self.sessionLocal()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()