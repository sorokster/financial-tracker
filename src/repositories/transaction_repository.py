from typing import Optional, List
from src.repositories.base_repository import BaseRepository
from src.models.transaction import Transaction


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
        cursor = self.client.execute(
            """
            INSERT INTO entries (type, amount, category, owner, date, description)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (transaction_type, amount, category, owner, date, description)
        )
        return cursor.lastrowid

    def get_transaction(self, transaction_id: int, owner: int) -> Optional[Transaction]:
        row = self.client.fetch_one(
            """
            SELECT t.id       AS transaction_id,
                   t.type     AS transaction_type,
                   t.amount,
                   t.date,
                   t.description,
                   t.category,
                   c.id       AS category_id,
                   c.name     AS category_name,
                   u.id       AS user_id,
                   u.email    AS user_email,
                   u.name     AS user_name,
                   u.surname  AS user_surname,
                   u.password AS user_password
            FROM entries t
                     JOIN categories c ON t.category = c.id
                     JOIN users u ON t.owner = u.id
            WHERE t.id = ?
              AND t.owner = ?
            """,
            (transaction_id, owner)
        )
        return Transaction.from_row(row) if row else None

    def get_transactions(self, owner: int, transaction_type: int) -> List[Transaction]:
        rows = self.client.fetch_all(
            """
            SELECT t.id       AS transaction_id,
                   t.type     AS transaction_type,
                   t.amount,
                   t.category,
                   t.date,
                   t.description,
                   c.id       AS category_id,
                   c.name     AS category_name,
                   u.id       AS user_id,
                   u.email    AS user_email,
                   u.name     AS user_name,
                   u.surname  AS user_surname,
                   u.password AS user_password
            FROM entries t
                     JOIN categories c ON t.category = c.id
                     JOIN users u ON t.owner = u.id
            WHERE u.id = ?
              AND t.type = ?
            """,
            (owner, transaction_type)
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
        cursor = self.client.execute(
            """
            UPDATE entries
            SET type        = ?,
                amount      = ?,
                category    = ?,
                date        = ?,
                description = ?
            WHERE id = ?
              AND owner = ?
            """,
            (transaction_type, amount, category, date, description, transaction_id, owner)
        )
        return cursor.rowcount > 0

    def remove_transaction(self, transaction_id: int, owner: int) -> bool:
        cursor = self.client.execute(
            """
            DELETE FROM entries 
            WHERE id = ? 
              AND owner = ?
            """,
            (transaction_id, owner)
        )
        return cursor.rowcount > 0
