from fastapi import APIRouter, Depends

from app.core.deps import require_token
from app.schemas.customer import (
    CustomerCreateIn,
    CustomerCreateOut,
    CustomerRead,
    LoanOfferCreate,
    LoanOfferRead,
)
from app.services.customer import CustomerService

customers_router = APIRouter(
    tags=["customers"], prefix="/customers", dependencies=[Depends(require_token)]
)
loanoffers_router = APIRouter(
    tags=["loanoffers"], prefix="/loanoffers", dependencies=[Depends(require_token)]
)

customer_service = CustomerService()


@customers_router.get(
    "/{id}", response_model=CustomerRead, summary="Retrieve a specific customer"
)
def get_customer(id: int):
    return customer_service.get_customer(customer_id=id)


@customers_router.post(
    "/", response_model=CustomerCreateOut, summary="Create a new customer"
)
def create_customer(payload: CustomerCreateIn):
    customer = customer_service.create_customer(
        first_name=payload.first_name, last_name=payload.last_name
    )
    return customer


@loanoffers_router.post(
    "/", response_model=LoanOfferRead, summary="Create a loan offer"
)
def create_loan_offer(payload: LoanOfferCreate):
    load_offer = customer_service.create_loan_offer(
        customer_id=payload.customer_id,
        amount=payload.amount,
        interest_rate=payload.interest_rate,
        term_months=payload.term_months,
    )
    return load_offer


@loanoffers_router.get(
    "/{id}", response_model=LoanOfferRead, summary="Retrieve a specific loan offer"
)
def get_loan_offer(id: int):
    return customer_service.get_loan_offer(loan_offer_id=id)
