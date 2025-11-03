from app.models.customer import Customer
from app.repositories.customer import CustomerRepository, LoanOfferRepository


class CustomerNotFoundError(Exception):
    pass


class LoanOfferNotFoundError(Exception):
    pass


class CustomerService:

    def get_customer(self, customer_id: int) -> Customer | None:
        with CustomerRepository() as customer_repository:
            customer = customer_repository.get(id=customer_id)
            if not customer:
                raise CustomerNotFoundError("Customer doesn't exist")
            return customer

    def create_customer(self, first_name: str, last_name: str) -> Customer:
        with CustomerRepository() as customer_repository:
            return customer_repository.create(first_name, last_name)

    @staticmethod
    def _compute_monthly_payment(
        amount: float, interest_rate: float, term_months: int
    ) -> float:
        # Standard loan amortization formula
        r = interest_rate / 100 / 12
        if r == 0:
            return amount / term_months
        return amount * (r * (1 + r) ** term_months) / ((1 + r) ** term_months - 1)

    def create_loan_offer(
        self, customer_id: int, amount: float, interest_rate: float, term_months: int
    ):
        self.get_customer(customer_id)  # Verify customer exists
        monthly_payment = CustomerService._compute_monthly_payment(
            amount, interest_rate, term_months
        )
        monthly_payment = round(monthly_payment, 2)
        with LoanOfferRepository() as loan_offer_repository:
            return loan_offer_repository.create_loan_offer(
                customer_id, amount, interest_rate, term_months, monthly_payment
            )

    def get_loan_offer(self, loan_offer_id: int):
        with LoanOfferRepository() as loan_offer_repository:
            load_offer = loan_offer_repository.get(id=loan_offer_id)
            if not load_offer:
                raise LoanOfferNotFoundError("Loan offer doesn't exist")
            return load_offer
