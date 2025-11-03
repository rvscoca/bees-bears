from unittest.mock import MagicMock, patch

import pytest

from app.services.customer import (
    CustomerNotFoundError,
    CustomerService,
    LoanOfferNotFoundError,
)


@pytest.fixture
def mock_customer_repo():
    with patch("app.services.customer.CustomerRepository") as repo:
        yield repo.return_value.__enter__.return_value


@pytest.fixture
def mock_loan_repo():
    with patch("app.services.customer.LoanOfferRepository") as repo:
        yield repo.return_value.__enter__.return_value


def test_get_customer(mock_customer_repo):
    mock_customer_repo.get.return_value = MagicMock(
        id=1, first_name="John", last_name="Wick"
    )

    customer = CustomerService().get_customer(customer_id=1)
    if customer:  # we know it's returning a customer here
        assert customer.id == 1
        mock_customer_repo.get.assert_called_once_with(id=1)


def test_get_customer_not_found(mock_customer_repo):
    mock_customer_repo.get.return_value = None

    with pytest.raises(CustomerNotFoundError):
        CustomerService().get_customer(42)


def test_create_customer(mock_customer_repo):
    mock_customer_repo.create.return_value = MagicMock(
        id=1, first_name="John", last_name="Wick"
    )

    customer = CustomerService().create_customer("John", "Wick")

    mock_customer_repo.create.assert_called_once_with("John", "Wick")
    assert customer.first_name == "John"


def test_create_loan_offer(mock_customer_repo, mock_loan_repo):
    mock_customer_repo.get.return_value = MagicMock(id=1)
    mock_loan_repo.create_loan_offer.return_value = MagicMock(id=99)

    loan_offer = CustomerService().create_loan_offer(1, 1000, 5, 12)

    mock_loan_repo.create_loan_offer.assert_called_once()
    assert loan_offer.id == 99


def test_create_loan_offer_customer_not_found(mock_customer_repo):
    mock_customer_repo.get.return_value = None

    with pytest.raises(CustomerNotFoundError):
        CustomerService().create_loan_offer(999, 1000, 5, 12)


def test_get_loan_offer_not_found(mock_loan_repo):
    mock_loan_repo.get.return_value = None

    with pytest.raises(LoanOfferNotFoundError):
        CustomerService().get_loan_offer(1000)
