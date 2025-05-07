# Banking Backend API

This project is a backend API for a banking system, built with FastAPI and PostgreSQL. It supports user authentication, account management, and transaction features for both bank employees and account holders.

## Features
- Secure login for employees and account holders
- Account creation, editing, and deletion (with business rules)
- Search for account holders by SSN (employee)
- Account holder self-service: view and edit details, transfer funds, view transactions
- Session management and strong password policies

## Tech Stack
- FastAPI
- SQLAlchemy
- Alembic (migrations)
- PostgreSQL (or SQLite for development)
- JWT Authentication

## Setup
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your database in `app/database.py`.
4. Run migrations:
   ```bash
   alembic upgrade head
   ```
5. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Folder Structure
- `app/` - Main application code
- `alembic/` - Database migrations

## Note
This project is backend only. No frontend is included. 