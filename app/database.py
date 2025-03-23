import pyodbc
from dotenv import load_dotenv
import os
from contextlib import contextmanager

load_dotenv()

class Database2:
    def __init__(self):
        self.connection = None
        
    def connect(self):
        if not self.connection or not self.is_connection_alive():
            self.connection = pyodbc.connect(
                f'DRIVER={os.getenv("AZURE_SQL_DRIVER")};'
                f'SERVER={os.getenv("AZURE_SQL_SERVER")};'
                f'DATABASE={os.getenv("AZURE_SQL_DATABASE")};'
                f'UID={os.getenv("AZURE_SQL_USERNAME")};'
                f'PWD={os.getenv("AZURE_SQL_PASSWORD")}'
            )
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def is_connection_alive(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            return True
        except pyodbc.Error:
            return False

    @contextmanager
    def get_cursor(self):
        self.connect()
        cursor = self.connection.cursor()
        try:
            yield cursor
        except Exception:
            self.connection.rollback()
            raise
        finally:
            cursor.close()