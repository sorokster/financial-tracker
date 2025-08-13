import hashlib
from src.models.user import User
from src.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, email: str, name: str, surname: str, password: str) -> User:
        user_id = self.repository.add_user(email, name, surname, self._hash_password(password))
        return self.repository.get_user_by_id(user_id)

    def authenticate(self, email: str, password: str) -> User | None:
        row = self.repository.get_user_by_email(email)
        if not row:
            return None

        user = User.from_row(row)
        if self._verify_password(password, user.password):
            return user
        return None

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def _verify_password(self, password: str, password_hash: str) -> bool:
        return self._hash_password(password) == password_hash