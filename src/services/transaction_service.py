from typing import Optional, List
from src.models.transaction import Transaction
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
        date: str,
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
        date: str,
        description: Optional[str] = None
    ) -> bool:
        return self.repository.update_transaction(
            transaction_id, transaction_type, amount, category, owner, date, description
        )

    def delete_transaction(self, transaction_id: int, owner: int) -> bool:
        return self.repository.remove_transaction(transaction_id, owner)

    def get_incomes(self, owner: int) -> List[Transaction]:
        return self.repository.get_transactions(owner, 1)

    def get_spends(self, owner: int) -> List[Transaction]:
        return self.repository.get_transactions(owner, 2)

    def get_income(self, transaction_id: int, owner) -> Optional[Transaction]:
        tx = self.repository.get_transaction(transaction_id, owner)
        return tx if tx and tx.type == 1 else None

    def get_spend(self, transaction_id: int, owner: int) -> Optional[Transaction]:
        tx = self.repository.get_transaction(transaction_id, owner)
        return tx if tx and tx.type == 2 else None