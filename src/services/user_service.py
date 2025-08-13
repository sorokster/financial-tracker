from src.models.user import User
from src.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, email: str, name: str, surname: str, password: str) -> User:
        self.repository.add_user(email, name, surname, password)
        return self.get_user(email)

    def get_user(self, email: str) -> User | None:
        row = self.repository.get_user_by_email(email)
        return User.from_row(row)

    def update_user(self, user_id: int, email: str, name: str, surname: str, password: str) -> bool:
        return self.repository.update_user(user_id, email, name, surname, password)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.remove_user(user_id)