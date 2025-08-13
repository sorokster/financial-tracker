from typing import Optional
from models import User
from src.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def add_user(self, email: str, name: str, surname: str, password: str) -> int:
        new_user = User(email=email, name=name, surname=surname, password=password)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user.id

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.session.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter(User.email == email).first()

    def update_user(self, user_id: int, email: str, name: str, surname: str, password: str) -> bool:
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        user.email = email
        user.name = name
        user.surname = surname
        user.password = password
        self.session.commit()
        return True

    def remove_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        self.session.delete(user)
        self.session.commit()
        return True