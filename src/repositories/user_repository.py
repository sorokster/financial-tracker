from src.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def add_user(self, email: str, name: str, surname: str, password: str) -> int:
        cursor = self.client.execute(
            """
            INSERT INTO users (email, name, surname, password)
            VALUES (?, ?, ?, ?)
            """,
            (email, name, surname, password)
        )
        return cursor.lastrowid

    def get_user_by_id(self, user_id: int):
        return self.client.fetch_one(
            """
            SELECT *
            FROM users
            WHERE id = ?
            """,
            (user_id,)
        )

    def get_user_by_email(self, email: str):
        return self.client.fetch_one(
            """
            SELECT *
            FROM users
            WHERE email = ?
            """,
            (email,)
        )

    def update_user(self, user_id: int, email: str, name: str, surname: str, password: str) -> bool:
        cursor = self.client.execute(
            """
            UPDATE users
            SET email = ?, name = ?, surname = ?, password = ?
            WHERE id = ?
            """,
            (email, name, surname, password, user_id)
        )
        return cursor.rowcount > 0

    def remove_user(self, user_id: int) -> bool:
        cursor = self.client.execute(
            """
            DELETE FROM users
            WHERE id = ?
            """,
            (user_id,)
        )
        return cursor.rowcount > 0