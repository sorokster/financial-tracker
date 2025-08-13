from datetime import datetime
from typing import Optional, List

from models import Transaction
from src.constants import INCOME, SPEND
from src.repositories.transaction_repository import TransactionRepository


class TransactionService:
    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def create_transaction(
        self,
        transaction_type: int,
        amount: float,
        category: int,
        owner: int,
        date: datetime,
        description: Optional[str] = None
    ) -> Transaction:
        transaction_id = self.repository.add_transaction(
            transaction_type, amount, category, owner, date, description
        )
        return self.repository.get_transaction(transaction_id, owner)

    def get_transaction(self, transaction_id: int, owner: int) -> Optional[Transaction]:
        return self.repository.get_transaction(transaction_id, owner)

    def get_transactions(self, owner: int, transaction_type: int) -> List[Transaction]:
        return self.repository.get_transactions(owner, transaction_type)

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
        return self.repository.update_transaction(
            transaction_id, transaction_type, amount, category, owner, date, description
        )

    def delete_transaction(self, transaction_id: int, owner: int) -> bool:
        return self.repository.remove_transaction(transaction_id, owner)

    def get_incomes(self, owner: int) -> List[Transaction]:
        return self.repository.get_transactions(owner, INCOME)

    def get_spends(self, owner: int) -> List[Transaction]:
        return self.repository.get_transactions(owner, SPEND)

    def get_income(self, transaction_id: int, owner) -> Optional[Transaction]:
        tx = self.repository.get_transaction(transaction_id, owner)
        return tx if tx and tx.type == INCOME else None

    def get_spend(self, transaction_id: int, owner: int) -> Optional[Transaction]:
        tx = self.repository.get_transaction(transaction_id, owner)
        return tx if tx and tx.type == SPEND else None