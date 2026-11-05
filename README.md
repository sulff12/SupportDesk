# SupportDesk

**A backend-focused helpdesk and ticket management system built with Python, FastAPI, PostgreSQL, and SQLAlchemy.**

SupportDesk is a learning-driven backend project designed to explore RESTful API development, relational databases, ORM architecture, containerization, and software engineering practices.

> **Project Status:** In active development.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | Object-Relational Mapping (ORM) |
| Pydantic | Data validation and serialization |
| Docker / Docker Compose | Containerized database environment |
| Git & GitHub | Version control |

## Project Goals

The goal of SupportDesk is to build a maintainable backend application for managing user support requests.

The project focuses on:

- Designing RESTful APIs with FastAPI
- Implementing CRUD operations
- Working with PostgreSQL using SQLAlchemy
- Understanding database sessions and transactions
- Organizing code into modular components
- Managing development environments with Docker
- Practicing Git workflows and version control

## Project Structure

```text
SupportDesk/
├── app/
│   ├── main.py
│   ├── database.py
│   └── tickets/
│       ├── models.py
│       ├── schemas.py
│       ├── router.py
│       └── service.py
├── create_table.py
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Architecture Overview

**`main.py`** — Initializes the FastAPI application and registers API routers.

**`database.py`** — Configures the SQLAlchemy engine, session factory, and declarative base.

**`models.py`** — Defines database tables through SQLAlchemy ORM models.

**`schemas.py`** — Defines Pydantic schemas for request validation and response serialization.

**`router.py`** — Defines API endpoints and handles HTTP requests.

**`service.py`** — Contains application logic for ticket operations.

**`create_table.py`** — Creates database tables from SQLAlchemy metadata during initial development.

## Database Model

The initial Ticket model contains:

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| title | String(200) | Ticket title |
| description | String(5000) | Detailed problem description |
| status | String(20) | Ticket status, defaults to `open` |

The database schema is managed through SQLAlchemy ORM during the initial development stage.

## Getting Started

### Prerequisites

- Python 3.10+
- Docker and Docker Compose
- Git

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/SupportDesk.git
cd SupportDesk
```

Replace `USERNAME` with the GitHub account that hosts this repository.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file using `.env.example` as a reference.

Configure `DATABASE_URL` with the PostgreSQL credentials, host, port, and database name matching your Docker Compose configuration.

Do not commit `.env` or real credentials to Git.

### 5. Start PostgreSQL

```bash
docker compose up -d
```

### 6. Initialize database tables

```bash
python create_table.py
```

### 7. Start the API

```bash
uvicorn app.main:app --reload
```

The API should be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## Development Roadmap

- [x] Initialize FastAPI project
- [x] Configure Docker and PostgreSQL
- [x] Establish SQLAlchemy database connection
- [x] Define initial Ticket ORM model
- [x] Create initial database table
- [ ] Implement database-backed ticket CRUD operations
- [ ] Add ticket status management
- [ ] Implement ticket categories
- [ ] Add database migrations with Alembic
- [ ] Implement authentication and authorization
- [ ] Add automated API tests
- [ ] Improve error handling and logging
- [ ] Prepare the application for deployment

## Learning Objectives

This project is also a practical exercise in understanding how production-style backend systems are structured.

Key learning areas include HTTP, dependency injection, database transactions, ORM model design, application architecture, testing, and Git workflows.

## License

No license has been specified yet.

---

**SupportDesk — a practical backend engineering project built step by step.**