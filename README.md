# AI-Based Legal Contract Analysis and Risk Detection System - Backend

Backend service built with FastAPI, SQLAlchemy, Alembic, and Python 3.11+ for legal contract analysis, clause extraction, and risk detection.

---

## Project Structure

```text
backend/
├── alembic/                 # Alembic migration environment
│   ├── versions/            # Migration scripts
│   └── env.py               # Alembic configuration (reads app Settings and Base.metadata)
├── alembic.ini              # Alembic project configuration
├── app/
│   ├── main.py              # FastAPI application instance, routes (/health)
│   ├── core/                # Configuration and database connection
│   │   ├── config.py        # Settings (loads DATABASE_URL from .env)
│   │   └── database.py      # SQLAlchemy engine, SessionLocal, Base, get_db()
│   ├── models/              # Database models (SQLAlchemy ORM)
│   │   ├── contract.py      # Contract model
│   │   ├── clause.py        # Clause model
│   │   └── risk.py          # Risk model
│   ├── schemas/             # Pydantic validation schemas
│   ├── crud/                # Database CRUD operations
│   ├── api/                 # API route handlers / controllers
│   └── services/            # Business logic and AI service integrations
├── tests/                   # Automated test suite
│   ├── test_health.py       # Health check tests
│   ├── test_database.py     # Database engine & session generator tests
│   └── test_models.py       # ORM model schema & relationship tests
├── .env.example             # Environment variable template
├── .env                     # Local environment settings
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation and setup instructions
```

---

## Getting Started

### Prerequisites

- **Python 3.11+** installed
- PostgreSQL 14+ (local service, Docker, or remote instance)
- `pip` package manager

---

### 1. Set Up Virtual Environment

From the `backend/` directory:

#### On Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### On Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Environment Configuration

Copy `.env.example` to `.env` if you haven't already:

#### Windows (PowerShell):
```powershell
Copy-Item .env.example .env
```

#### Linux / macOS:
```bash
cp .env.example .env
```

Edit `.env` with your actual PostgreSQL connection string:
```env
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
```

---

### 4. Run Database Migrations

Apply Alembic migrations to create all database tables and constraints:

```bash
alembic upgrade head
```

---

### 5. Run Development Server

Start the application with hot reload:

```bash
python -m uvicorn app.main:app --reload
```

The server will be available at:
- **API Base URL**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### 6. Verify Health Route

In a separate terminal or browser:
```bash
curl http://127.0.0.1:8000/health
```
Expected response:
```json
{"status": "ok"}
```

---

### 7. Database Migrations Reference

To generate new migrations after updating ORM models:
```bash
alembic revision --autogenerate -m "migration description"
```

To apply pending migrations:
```bash
alembic upgrade head
```

To rollback the last migration:
```bash
alembic downgrade -1
```

---

### 8. Running Automated Tests

Run the test suite with `pytest`:

```bash
pytest
```
All automated tests will run and verify endpoints, database components, and ORM model schemas.
