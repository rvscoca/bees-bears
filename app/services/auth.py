from app.core.security import create_token, hash_password, verify_password
from app.repositories.user import UserRepository
from app.schemas.auth import UserCreate


class UsernameAlreadyTakenError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class AuthService:

    def register_user(self, user_data: UserCreate):
        username = user_data.username
        with UserRepository() as user_repository:
            if user_repository.get(username=username):
                raise UsernameAlreadyTakenError("Username already taken")
            hashed_pw = hash_password(user_data.password)
            return user_repository.create(
                name=user_data.username, hashed_password=hashed_pw
            )

    def login_user(self, username, password) -> str:
        with UserRepository() as user_repository:
            user = user_repository.get(username=username)
            if not user or not verify_password(password, user.hashed_password):
                raise InvalidCredentialsError("Invalid username or password")
            return create_token({"name": user.username})
