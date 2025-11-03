from sqlmodel import select

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    def get(self, **filters):
        stmt = select(User).filter_by(**filters)
        user = self.session.exec(stmt).first()
        return user

    def create(self, name: str, hashed_password: str):
        user = User(username=name, hashed_password=hashed_password)
        self.session.add(user)
        self.commit()
        self.session.refresh(user)
        return user
