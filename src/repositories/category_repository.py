from typing import List, Tuple

from src.models.category import Category
from src.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def add_category(self, name: str, owner: int) -> int:
        cursor = self.client.execute(
            """
            INSERT INTO categories (name, owner)
            VALUES (?, ?)
            """,
            (name, owner),
        )
        self.client.connection.commit()
        return cursor.lastrowid

    def get_categories(self, owner: int) -> List[Tuple] | None:
        return self.client.fetch_all(
            """
            SELECT
                c.id AS category_id,
                c.name AS category_name,
                c.owner,
                u.id AS user_id,
                u.email AS user_email,
                u.name AS user_name,
                u.surname AS user_surname,
                u.password AS user_password
            FROM categories c
            JOIN users u ON c.owner = u.id
            WHERE c.owner = ?
            """,
            (owner,)
        )

    def get_category(self, category: int, owner: int) -> Category | None:
        return self.client.fetch_one(
            """
            SELECT
                c.id AS category_id,
                c.name AS category_name,
                c.owner,
                u.id AS user_id,
                u.email AS user_email,
                u.name AS user_name,
                u.surname AS user_surname,
                u.password AS user_password
            FROM categories c
            JOIN users u ON c.owner = u.id
            WHERE c.id = ? 
              AND c.owner = ?
            """,
            (category, owner)
        )

    def update_category(self, category: int, name: str, owner: int) -> bool:
        cursor = self.client.execute(
            """
            UPDATE categories
            SET name = ?
            WHERE id = ? 
              AND owner = ?
            """,
            (name, category, owner)
        )
        return cursor.rowcount > 0

    def remove_category(self, category: int, owner: int) -> bool:
        cursor = self.client.execute(
            """
            DELETE FROM categories
            WHERE id = ? AND owner = ?
            """,
            (category, owner)
        )
        return cursor.rowcount > 0