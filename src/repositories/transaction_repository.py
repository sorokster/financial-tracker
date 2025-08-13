from datetime import datetime
from typing import Optional, List
from models import Transaction, Category, User
from src.repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository):
    def add_transaction(
        self,
        transaction_type: int,
        amount: float,
        category: int,
        owner: int,
        date: datetime,
        description: Optional[str] = None
    ) -> int:
        new_transaction = Transaction(
            type=transaction_type,
            amount=amount,
            category=category,
            owner=owner,
            date=date,
            description=description
        )
        self.session.add(new_transaction)
        self.session.commit()
        self.session.refresh(new_transaction)
        return new_transaction.id

    def get_transaction(self, transaction_id: int, owner: int) -> Optional[Transaction]:
        return (
            self.session.query(Transaction)
            .join(Category, Transaction.category == Category.id)
            .join(User, Transaction.owner == User.id)
            .filter(Transaction.id == transaction_id, Transaction.owner == owner)
            .first()
        )

    def get_transactions(self, owner: int, transaction_type: int) -> List[Transaction]:
        return (
            self.session.query(Transaction)
            .join(Category, Transaction.category == Category.id)
            .join(User, Transaction.owner == User.id)
            .filter(User.id == owner, Transaction.type == transaction_type)
            .all()
        )

    def update_transaction(
        self,
        transaction_id: int,
        transaction_type: int,
        amount: float,
        category: int,
        owner: int,
        date: datetime,
        description: Optional[str] = None
    ) -> bool:
        transaction = self.get_transaction(transaction_id, owner)
        if not transaction:
            return False
        transaction.type = transaction_type
        transaction.amount = amount
        transaction.category = category
        transaction.date = date
        transaction.description = description
        self.session.commit()
        return True

    def remove_transaction(self, transaction_id: int, owner: int) -> bool:
        transaction = self.get_transaction(transaction_id, owner)
        if not transaction:
            return False
        self.session.delete(transaction)
        self.session.commit()
        return True