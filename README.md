# Notes-app-Backend

A personal notes API built with FastAPI and PostgreSQL. Supports user auth with JWT and full CRUD on notes — each user only ever sees their own.

Built this to get my hands dirty with backend development. No fluff, just a clean working API.

---

## Stack

FastAPI · PostgreSQL · SQLAlchemy · Alembic · JWT · bcrypt · Pydantic

---

## What it does

- Signup / Login with hashed passwords
- JWT auth with expiry
- Create, read, update, delete notes
- Users can only touch their own notes

---

## Endpoints

```
POST   /signup          Register
POST   /login           Get JWT token

POST   /notes           Create a note
GET    /notes           Get your notes
GET    /notes/{id}      Get one note
PUT    /notes/{id}      Update a note
DELETE /notes/{id}      Delete a note
```

All `/notes` routes require `Authorization: Bearer <token>` in the header.

---

## Run it locally

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd notes-app

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```
DATABASE_URL=postgresql://username:password@localhost:5432/notesapp
SECRET_KEY=your_secret_key
```

```bash
alembic upgrade head
uvicorn main:app --reload
```

Swagger UI at `http://127.0.0.1:8000/docs`

---

## Live API
