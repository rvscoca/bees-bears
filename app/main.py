from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.exception_handlers import register_exception_handlers

from .api import auth, customer
from .database.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Bees & Bears mini API",
    description="API for managing **customers** and **loan offers**",
    version="1.0.0",
)

register_exception_handlers(app)

app.include_router(auth.router)
app.include_router(customer.customers_router)
app.include_router(customer.loanoffers_router)
