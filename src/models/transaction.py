import datetime
from typing import Optional
from src.models.category import Category
from src.models.user import User


class Transaction:
    def __init__(
        self,
        transaction_type: str,
        amount: float,
        category: Category,
        owner: User,
        date: datetime.datetime,
        description: Optional[str] = None,
        transaction_id: Optional[int] = None,
    ):
        self.id = transaction_id
        self.type = transaction_type
        self.amount = amount
        self.description = description
        self.category = category
        self.owner = owner
        self.date = date

    def __repr__(self):
        return (
            f"Transaction(id={self.id}, type='{self.type}', description='{self.description}', "
            f"amount={self.amount}, category={self.category}, owner={self.owner}, date={self.date})"
        )

    @classmethod
    def from_row(cls, row):
        if row is None:
            return None

        owner = User(
            user_id=row["user_id"],
            email=row["user_email"],
            name=row["user_name"],
            surname=row["user_surname"],
            password=row["user_password"]
        )

        category = Category(
            category_id=row["category_id"],
            name=row["category_name"],
            owner=owner
        )

        return cls(
            transaction_type=row["transaction_type"],
            amount=row["amount"],
            category=category,
            owner=owner,
            date=row["date"],
            description=row["description"],
            transaction_id=row["transaction_id"]
        )