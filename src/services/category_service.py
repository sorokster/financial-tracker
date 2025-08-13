from typing import List
from models import Category
from src.repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def create_category(self, name: str, owner: int) -> Category:
        row = self.repository.add_category(name, owner)
        return self.get_category(row, owner)

    def get_categories(self, owner: int) -> List[Category]:
        return self.repository.get_categories(owner)

    def get_category(self, category: int, owner: int) -> Category | None:
        return self.repository.get_category(category, owner)

    def update_category(self, category: int, name: str, owner: int) -> bool:
        return self.repository.update_category(category, name, owner)

    def delete_category(self, category: int, user_id: int) -> bool:
        return self.repository.remove_category(category, user_id)