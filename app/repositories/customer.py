from sqlmodel import select

from app.models.customer import Customer, LoanOffer
from app.repositories.base import BaseRepository


class CustomerRepository(BaseRepository):

    def get(self, **filters):
        stmt = select(Customer).filter_by(**filters)
        customer = self.session.exec(stmt).first()
        return customer

    def create(self, first_name: str, last_name: str) -> Customer:
        customer = Customer(first_name=first_name, last_name=last_name)
        self.session.add(customer)
        self.commit()
        self.session.refresh(customer)
        return customer


class LoanOfferRepository(BaseRepository):

    def create_loan_offer(
        self,
        customer_id: int,
        amount: float,
        interest_rate: float,
        term_months: int,
        monthly_payment: float,
    ):
        loan_offer = LoanOffer(
            customer_id=customer_id,
            amount=amount,
            interest_rate=interest_rate,
            term_months=term_months,
            monthly_payment=monthly_payment,
        )
        self.session.add(loan_offer)
        self.commit()
        self.session.refresh(loan_offer)
        return loan_offer

    def get(self, **filters):
        stmt = select(LoanOffer).filter_by(**filters)
        loan_offer = self.session.exec(stmt).first()
        return loan_offer
