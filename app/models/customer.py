from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    loans: List["LoanOffer"] = Relationship(
        back_populates="customer",
        sa_relationship_kwargs={"lazy": "joined", "cascade": "all, delete-orphan"},
    )


class LoanOffer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    amount: float
    interest_rate: float
    term_months: int
    monthly_payment: float
    customer: Optional[Customer] = Relationship(back_populates="loans")
