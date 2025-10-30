# 🐝 Bees & Bears

A FastAPI project built as a technical test. 

## ⚙️ Requirements

- **Python 3.13+**
- **uv**

Install uv with pip:
```bash
pip install uv
```

---

## 🚀 Setup

Clone the project and install dependencies:
```bash
git clone git@github.com:rvscoca/bees-bears.git
cd bees_and_bears
uv sync
```

---

## 🔐 Environment

Generate a secure secret key:
```bash
uv run python -c "import secrets; print(secrets.token_hex(32))"
```

Replace the dummy SECRET_KEY value in the `.env.template`:
```
SECRET_KEY="YOUR_NEWLY_GENERATED_SECRET_KEY"
```
you can also change the algorithm if you want, but it is not necessary.

Copy it:
```bash
cp .env.template .env
```

---

## 🧱 Database

The app uses **SQLite**.  
Tables are created automatically at startup; there is no migrations needed.

To reset the database:
```bash
rm app/database/database.db
```

---

## 🏃 Run the Application

Start the FastAPI server:
```bash
uv run uvicorn app.main:app --reload
```

Server available at:
- **http://localhost:8000**
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Run Tests

Run all tests with coverage:
```bash
uv run pytest --cov=app
```

All repositories are mocked, no real database is needed for the unit tests.

---

## 📁 Project Structure

```
app/
├── api/           # Routers
├── core/          # authentication, exception handlers, config
├── models/        # Database models
├── repositories/  # Persistence
├── services/      # Business logic
├── schemas/       # Pydantic schemas
└── main.py        # App entrypoint
tests/
└── test_customer_service.py
```

---

## 🧠 Design

- **DDD architecture:** domain logic isolated in `services/`, persistence in `repositories/`, and routes in `api/`
- Layered and separated (Repository → Service → Router)
- JWT authentication with Bearer tokens
- Centralized error handling
- Mocks used for tests (DB-independent execution)
