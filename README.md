# Notes App Backend

A full-stack Notes application backend built with **FastAPI** and **PostgreSQL** featuring JWT authentication, secure password hashing, and complete CRUD operations. Each user can only access and manage their own notes through protected API endpoints.

Built as my first backend project to understand REST APIs, authentication, database design, ORM, migrations, and deployment from scratch.

---

## Tech Stack

- FastAPI
- PostgreSQL (Neon)
- SQLAlchemy
- Alembic
- Pydantic
- JWT Authentication
- bcrypt (Password Hashing)
- Uvicorn
- Render (Backend Deployment)
- Vercel (Frontend Deployment)

---

## Features

- User registration with hashed passwords
- Secure login using JWT authentication
- Protected API endpoints
- Create, Read, Update & Delete notes
- User-specific note ownership
- Database migrations using Alembic
- RESTful API design
- CORS enabled for frontend integration

---

## Live Demo

### Frontend
 https://lemme-take-some-notes.vercel.app

### Backend API
 https://notesapp-backend-8pzp.onrender.com

### API Documentation (Swagger)
 https://notesapp-backend-8pzp.onrender.com/docs

> **Note:** The backend is hosted on Render's free tier. The first request after inactivity may take around 30–60 seconds while the server wakes up.

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/signup` | Register a new user |
| POST | `/login` | Login and receive JWT token |

### Notes

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/notes` | Create a note |
| GET | `/notes` | Get all notes for the logged-in user |
| GET | `/notes/{id}` | Get a specific note |
| PUT | `/notes/{id}` | Update a note |
| DELETE | `/notes/{id}` | Delete a note |

All **/notes** endpoints require:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## Project Structure

```
backend-notesapp/
│
├── routes/
│   ├── users.py
│   └── notes.py
│
├── alembic/
│
├── auth.py
├── database.py
├── main.py
├── models.py
├── schemas.py
├── requirements.txt
└── .env
```

---

## Run Locally

Clone the repository

```bash
git clone https://github.com/ujwalshetty625/notesapp-backend.git
cd notesapp-backend
```

Create and activate a virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
DATABASE_URL=postgresql://username:password@localhost:5432/notesapp
SECRET_KEY=your_secret_key
```

Run database migrations

```bash
alembic upgrade head
```

Start the server

```bash
uvicorn main:app --reload
```

Visit:

```
http://127.0.0.1:8000/docs
```

---

## What I Learned

This project helped me understand:

- FastAPI architecture
- REST API development
- SQLAlchemy ORM
- PostgreSQL integration
- JWT authentication
- Password hashing with bcrypt
- Database migrations using Alembic
- Dependency Injection (`Depends`)
- CORS configuration
- Backend deployment using Render
- Frontend deployment using Vercel
- Integrating a frontend with a production backend

---

## Future Improvements

- Search notes
- Categories / Tags
- Rich text editor
- File attachments
- Rate limiting
- Unit tests
- Docker support
- CI/CD with GitHub Actions
