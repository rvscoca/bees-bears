from unittest.mock import MagicMock, patch

import pytest

from app.schemas.auth import UserCreate
from app.services.auth import (
    AuthService,
    UsernameAlreadyTakenError,
)


@pytest.fixture
def user_data():
    return UserCreate(username="George", password="pw")


def test_register_user_success(user_data):
    with (
        patch("app.services.auth.UserRepository") as mock_repo,
        patch("app.services.auth.hash_password", return_value="hashed_pw") as mock_hash,
    ):

        repo = mock_repo.return_value.__enter__.return_value
        repo.get.return_value = None
        repo.create.return_value = MagicMock(username="George")

        user = AuthService().register_user(user_data)

        repo.get.assert_called_once_with(username="George")
        repo.create.assert_called_once_with(name="George", hashed_password="hashed_pw")
        mock_hash.assert_called_once_with("pw")
        assert user.username == "George"


def test_register_user_username_taken(user_data):
    with patch("app.services.auth.UserRepository") as mock_repo:
        repo = mock_repo.return_value.__enter__.return_value
        repo.get.return_value = MagicMock(username="George")

        with pytest.raises(UsernameAlreadyTakenError):
            AuthService().register_user(user_data)


def test_login_user_success():
    with (
        patch("app.services.auth.UserRepository") as mock_repo,
        patch("app.services.auth.verify_password", return_value=True),
        patch("app.services.auth.create_token", return_value="fake_token"),
    ):

        repo = mock_repo.return_value.__enter__.return_value
        repo.get.return_value = MagicMock(username="George", hashed_password="hashed_pw")

        token = AuthService().login_user("George", "pw")

        assert token == "fake_token"
        repo.get.assert_called_once_with(username="George")
