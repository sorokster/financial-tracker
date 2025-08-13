from abc import ABC
from src.database.client import Client
from src.database.sqlite_client import SQLiteClient


class DatabaseConnectionFactory(Client, ABC):
    @staticmethod
    def create_client(db_type: str, **params) -> Client:
        db_type = db_type.lower()
        if db_type == 'sqlite':
            db_name = params.get('db_name')
            if not db_name:
                raise ValueError("Parameter 'db_name' required for SQLite")
            return SQLiteClient(db_name=db_name)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")