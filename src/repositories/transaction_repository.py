from typing import Optional, List
from src.models.transaction import Transaction
from src.repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository):
    def add_transaction(
        self,
        transaction_type: int,
        amount: float,
        category: int,
        owner: int,
        date: str,
        description: Optional[str] = None
    ) -> int:
        return self.insert(
            "entries",
            {
                "type": transaction_type,
                "amount": amount,
                "category": category,
                "owner": owner,
                "date": date,
                "description": description
            }
        )

    def get_transaction(self, transaction_id: int, owner: int) -> Optional[Transaction]:
        row = self.select_one(
            table="entries t",
            columns=[
                "t.id AS transaction_id",
                "t.type AS transaction_type",
                "t.amount",
                "t.date",
                "t.description",
                "t.category",
                "c.id AS category_id",
                "c.name AS category_name",
                "u.id AS user_id",
                "u.email AS user_email",
                "u.name AS user_name",
                "u.surname AS user_surname",
                "u.password AS user_password"
            ],
            join="JOIN categories c ON t.category = c.id "
                 "JOIN users u ON t.owner = u.id",
            where="t.id = ? AND t.owner = ?",
            params=(transaction_id, owner)
        )
        return Transaction.from_row(row) if row else None

    def get_transactions(self, owner: int, transaction_type: int) -> List[Transaction]:
        rows = self.select(
            table="entries t",
            columns=[
                "t.id AS transaction_id",
                "t.type AS transaction_type",
                "t.amount",
                "t.category",
                "t.date",
                "t.description",
                "c.id AS category_id",
                "c.name AS category_name",
                "u.id AS user_id",
                "u.email AS user_email",
                "u.name AS user_name",
                "u.surname AS user_surname",
                "u.password AS user_password"
            ],
            join="JOIN categories c ON t.category = c.id "
                 "JOIN users u ON t.owner = u.id",
            where="u.id = ? AND t.type = ?",
            params=(owner, transaction_type)
        )
        return [Transaction.from_row(row) for row in rows]

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
        return self.update(
            table="entries",
            data={
                "type": transaction_type,
                "amount": amount,
                "category": category,
                "date": date,
                "description": description
            },
            where="id = ? AND owner = ?",
            params=(transaction_id, owner)
        )

    def remove_transaction(self, transaction_id: int, owner: int) -> bool:
        return self.delete(
            table="entries",
            where="id = ? AND owner = ?",
            params=(transaction_id, owner)
        )