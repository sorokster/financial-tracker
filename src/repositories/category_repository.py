from typing import Optional, List
from models import Category, User
from src.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def add_category(self, name: str, owner: int) -> int:
        new_category = Category(name=name, owner=owner)
        self.session.add(new_category)
        self.session.commit()
        self.session.refresh(new_category)
        return new_category.id

    def get_categories(self, owner: int) -> List[Category]:
        return (
            self.session.query(Category)
            .join(User, Category.owner == User.id)
            .filter(Category.owner == owner)
            .all()
        )

    def get_category(self, category_id: int, owner: int) -> Optional[Category]:
        return (
            self.session.query(Category)
            .join(User, Category.owner == User.id)
            .filter(Category.id == category_id, Category.owner == owner)
            .first()
        )

    def update_category(self, category_id: int, name: str, owner: int) -> bool:
        category = self.get_category(category_id, owner)
        if not category:
            return False
        category.name = name
        self.session.commit()
        return True

    def remove_category(self, category_id: int, owner: int) -> bool:
        category = self.get_category(category_id, owner)
        if not category:
            return False
        self.session.delete(category)
        self.session.commit()
        return True