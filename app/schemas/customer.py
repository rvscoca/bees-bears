from typing import List

from pydantic import BaseModel


# Loan offer schemas
class LoanOfferRead(BaseModel):
    id: int
    amount: float
    interest_rate: float
    term_months: int
    monthly_payment: float


class LoanOfferCreate(BaseModel):
    customer_id: int
    amount: float
    interest_rate: float
    term_months: int


# Customer schemas
class CustomerCreateIn(BaseModel):
    first_name: str
    last_name: str


class CustomerCreateOut(BaseModel):
    id: int
    first_name: str
    last_name: str


class CustomerRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    loans: List[LoanOfferRead] = []
