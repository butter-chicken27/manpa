from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = (
    f"mssql+pyodbc://{os.getenv('AZURE_SQL_USERNAME')}:"
    f"{os.getenv('AZURE_SQL_PASSWORD')}@"
    f"{os.getenv('AZURE_SQL_SERVER')}/"
    f"{os.getenv('AZURE_SQL_DATABASE')}?"
    f"driver={os.getenv('AZURE_SQL_DRIVER')}"
)