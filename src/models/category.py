from typing import Optional
from src.models.user import User


class Category:
    def __init__(self, name: str, owner: User, category_id: Optional[int] = None):
        self.id = category_id
        self.name = name
        self.owner = owner

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}', owner_id={self.owner.id}), owner_name={self.owner.name}, owner_surname={self.owner.surname}))"

    @classmethod
    def from_row(cls, row):
        if row is None:
            return None

        user = User(
            user_id=row["user_id"],
            email=row["user_email"],
            name=row["user_name"],
            surname=row["user_surname"],
            password=row["user_password"]
        )

        return cls(
            category_id=row["category_id"],
            name=row["category_name"],
            owner=user
        )