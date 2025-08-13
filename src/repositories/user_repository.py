from typing import Optional

from src.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def add_user(self, email: str, name: str, surname: str, password: str) -> int:
        return self.insert(
            "users",
            {"email": email, "name": name, "surname": surname, "password": password}
        )

    def get_user_by_id(self, user_id: int) -> Optional[dict]:
        return self.select_one(
            table="users",
            where="id = ?",
            params=(user_id,)
        )

    def get_user_by_email(self, email: str) -> Optional[dict]:
        return self.select_one(
            table="users",
            where="email = ?",
            params=(email,)
        )

    def update_user(self, user_id: int, email: str, name: str, surname: str, password: str) -> bool:
        return self.update(
            table="users",
            data={"email": email, "name": name, "surname": surname, "password": password},
            where="id = ?",
            params=(user_id,)
        )

    def remove_user(self, user_id: int) -> bool:
        return self.delete(
            table="users",
            where="id = ?",
            params=(user_id,)
        )