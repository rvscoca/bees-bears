from sqlmodel import Session, SQLModel, create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///app/database/{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=False)


def init_db():
    print("Initializing database...")
    from app.models.customer import Customer  # noqa: F401
    from app.models.customer import LoanOffer  # noqa: F401
    from app.models.user import User  # noqa: F401

    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
