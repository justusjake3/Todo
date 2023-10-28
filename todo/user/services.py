from ..todo.models import User
from ..todo.database import SessionLocal
from typing import List


class UserServices:
    def __init__(self) -> None:
        self.database = SessionLocal()

    def create_user(self, user_data) -> User:
        user = User(
            name=user_data.name,
            email=user_data.email,
            hashed_password=user_data.hashed_password,
            )
        self.database.add(user)
        self.database.commit()
        self.database.refresh(user)
        return user

    def get_all_users(self) -> List[User]:
        users = self.database.query(User).all()
        return users

    def get_user_by_id(self, user_id) -> User:
        user = self.database.query(User).filter(User.id == user_id).first()
        return user