from typing import List
from src.models.category import Category
from src.repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def create_category(self, name: str, owner: int) -> Category:
        row = self.repository.add_category(name, owner)
        return self.get_category(row, owner)

    def get_categories(self, owner: int) -> List[Category]:
        rows = self.repository.get_categories(owner)
        return [Category.from_row(row) for row in rows]

    def get_category(self, category: int, owner: int) -> Category | None:
        row = self.repository.get_category(category, owner)
        return Category.from_row(row)

    def update_category(self, category: int, name: str, owner: int) -> bool:
        return self.repository.update_category(category, name, owner)

    def delete_category(self, category: int, user_id: int) -> bool:
        return self.repository.remove_category(category, user_id)