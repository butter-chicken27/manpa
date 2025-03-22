import pyodbc
from dotenv import load_dotenv
import os
from contextlib import contextmanager

load_dotenv()

class Database2:
    def __init__(self):
        self.connection = None
        
    def connect(self):
        if not self.connection:
            self.connection = pyodbc.connect(
                'DRIVER={ODBC Driver 18 for SQL Server};'
                f'SERVER={os.getenv("AZURE_SQL_SERVER")};'
                f'DATABASE={os.getenv("AZURE_SQL_DATABASE")};'
                f'UID={os.getenv("AZURE_SQL_USERNAME")};'
                f'PWD={os.getenv("AZURE_SQL_PASSWORD")}'
            )
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    @contextmanager
    def get_cursor(self):
        cursor = self.connection.cursor()
        try:
            yield cursor
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            raise