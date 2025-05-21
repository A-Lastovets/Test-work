# 📚 Book Management App

A simple web application for managing a list of books using **FastAPI**, **Jinja2 templates**, **PostgreSQL**, and **Docker**.

---

## ✨ Features

- View all books  
- Filter books by year, author, or price  
- Add new books via modal form  
- Delete books  
- Server-side rendered UI with Bootstrap  
- Dockerized deployment  

---

## 🚀 Tech Stack

- **Backend**: FastAPI  
- **Frontend**: Jinja2 + Bootstrap 5  
- **Database**: PostgreSQL  
- **ORM**: SQLAlchemy  
- **Environment**: Docker, dotenv  

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/book-app.git
cd book-app
```

### 2. Configure `.env`

Create a `.env` file:

```env
DATABASE_URL=postgresql://user:password@db:5432/books_db
```

> Replace `user`, `password`, and `books_db` with your actual PostgreSQL credentials.

---

### 3. Run with Docker

```bash
docker-compose up --build -d
```

Open the app in your browser:  
📂 http://localhost:8000  
📑 Swagger UI: http://localhost:8000/docs  

---

## 🧪 API Endpoints

| Method | Path                   | Description        |
|--------|------------------------|--------------------|
| GET    | `/api/book`            | List/filter books  |
| POST   | `/api/book`            | Add a book         |
| DELETE | `/api/book/{book_id}`  | Delete a book      |

---
