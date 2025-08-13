from src.models.category import Category
from src.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def add_category(self, name: str, owner: int) -> int:
        return self.insert("categories", {"name": name, "owner": owner})

    def get_categories(self, owner: int):
        return self.select(
            table="categories c",
            columns=[
                "c.id AS category_id",
                "c.name AS category_name",
                "c.owner",
                "u.id AS user_id",
                "u.email AS user_email",
                "u.name AS user_name",
                "u.surname AS user_surname",
                "u.password AS user_password",
            ],
            join="JOIN users u ON c.owner = u.id",
            where="c.owner = ?",
            params=(owner,)
        )

    def get_category(self, category: int, owner: int) -> Category | None:
        return self.select_one(
            table="categories c",
            columns=[
                "c.id AS category_id",
                "c.name AS category_name",
                "c.owner",
                "u.id AS user_id",
                "u.email AS user_email",
                "u.name AS user_name",
                "u.surname AS user_surname",
                "u.password AS user_password",
            ],
            join="JOIN users u ON c.owner = u.id",
            where="c.id = ? AND c.owner = ?",
            params=(category, owner)
        )

    def update_category(self, category: int, name: str, owner: int) -> bool:
        return self.update(
            table="categories",
            data={"name": name},
            where="id = ? AND owner = ?",
            params=(category, owner)
        )

    def remove_category(self, category: int, owner: int) -> bool:
        return self.delete(
            table="categories",
            where="id = ? AND owner = ?",
            params=(category, owner)
        )