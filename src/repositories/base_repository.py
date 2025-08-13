from typing import Union, Optional, Tuple, List, Dict, Any

from src.database.client import Client


class BaseRepository:
    def __init__(self, client: Client):
        self.client = client

    def insert(self, table: str, data: Dict[str, Any]) -> int:
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        values = tuple(data.values())

        cursor = self.client.execute(
            f"INSERT INTO {table} ({columns}) VALUES ({placeholders})",
            values
        )
        self.client.connection.commit()
        return cursor.lastrowid

    def select(
        self,
        table: str,
        columns: Union[str, List[str]] = "*",
        where: Optional[str] = None,
        params: Tuple = (),
        join: Optional[str] = None
    ) -> List[Tuple]:
        if isinstance(columns, list):
            columns = ", ".join(columns)

        query = f"SELECT {columns} FROM {table}"
        if join:
            query += f" {join}"
        if where:
            query += f" WHERE {where}"

        return self.client.fetch_all(query, params)

    def select_one(
        self,
        table: str,
        columns: Union[str, List[str]] = "*",
        where: Optional[str] = None,
        params: Tuple = (),
        join: Optional[str] = None
    ) -> Optional[Tuple]:
        if isinstance(columns, list):
            columns = ", ".join(columns)

        query = f"SELECT {columns} FROM {table}"
        if join:
            query += f" {join}"
        if where:
            query += f" WHERE {where}"

        return self.client.fetch_one(query, params)

    def update(self, table: str, data: Dict[str, Any], where: str, params: Tuple) -> bool:
        set_clause = ", ".join([f"{k} = ?" for k in data.keys()])
        values = tuple(data.values()) + params
        cursor = self.client.execute(
            f"UPDATE {table} SET {set_clause} WHERE {where}",
            values
        )
        self.client.connection.commit()
        return cursor.rowcount > 0

    def delete(self, table: str, where: str, params: Tuple) -> bool:
        cursor = self.client.execute(
            f"DELETE FROM {table} WHERE {where}",
            params
        )
        self.client.connection.commit()
        return cursor.rowcount > 0