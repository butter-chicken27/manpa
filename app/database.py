from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

class Database:
    def __init__(self):
        self.engine = None
        self.sessionLocal  = None

    def connect(self):
        if not self.engine or not self.sessionLocal or not self.is_connected():
            if self.engine:
                self.engine.dispose()
                self.engine = None
                self.sessionLocal = None
                
            self.engine = create_engine(
                DATABASE_URL,
                pool_pre_ping=True,
                pool_recycle=3600,
                pool_size=20,
                max_overflow=10,
                connect_args={"connect_timeout": 30}
            )
            self.sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
    def disconnect(self):
        if self.engine:
            self.engine.dispose()
            self.engine = None
            self.sessionLocal = None
    
    def is_connected(self):
        if self.engine:
            try:
                with self.engine.connect() as conn:
                    conn.execute("SELECT 1")
                return True
            except Exception:
                return False
        return False

    @contextmanager
    def getSession(self):
        self.connect()
        if not self.sessionLocal:
            raise Exception("Database not connected")
        session = self.sessionLocal()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()