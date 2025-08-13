import sqlite3
from typing import Any, List, Optional, Tuple
from contextlib import contextmanager
from src.database.client import Client


class SQLiteClient(Client):
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        super().__init__(db_name=db_name)

    def connect(self, **kwargs) -> None:
        if self.connection is None:
            db_name = kwargs.get('db_name', self.db_name)
            self.connection = sqlite3.connect(db_name)
            self.connection.row_factory = sqlite3.Row

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None

    def __del__(self) -> None:
        self.close()

    @contextmanager
    def _get_cursor(self):
        if not self.connection:
            raise RuntimeError("Database connection is not established.")
        cursor = self.connection.cursor()
        try:
            yield cursor
        finally:
            cursor.close()

    def execute(self, query: str, params: Optional[Tuple] = None) -> sqlite3.Cursor:
        if params is None:
            params = ()
        with self._get_cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor

    def fetch_all(self, query: str, params: Optional[Tuple] = None) -> List[Tuple]:
        if params is None:
            params = ()
        with self._get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def fetch_one(self, query: str, params: Optional[Tuple] = None) -> Any:
        if params is None:
            params = ()
        with self._get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()