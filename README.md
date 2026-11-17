# Student Management System using FastAPI

## Project Overview

The **Student Management System** is a web-based application developed using Python and FastAPI to manage student information efficiently. It allows users to perform CRUD (Create, Read, Update, Delete) operations and manage student attendance.

This project was developed as part of my Python Full Stack Development learning journey to gain practical experience with FastAPI fundamentals and backend development.

## Features

- **Add Student:** Register new students with their personal and academic details.
- **View Students:** Display all registered students on the dashboard.
- **Student Profile:** View individual student information.
- **Update Student:** Edit existing student details.
- **Delete Student:** Remove student records from the database.
- **Attendance Management:** Set and display student attendance as Present or Absent.
- **Dynamic Templates:** Display database information using Jinja2 templates.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web framework |
| SQLite | Database management |
| HTML | Web page structure |
| CSS | Styling and UI design |
| Jinja2 | Dynamic HTML templates |
| Pydantic | Data validation |

## Project Structure

```text
Student-Management-System/
│
├── main.py
│
├── students.db
│
└── templates/
    ├── home.html
    ├── add.html
    ├── edit.html
    └── std.html
```

## CRUD Operations

1. **Create:** Add new student records.
2. **Read:** Retrieve and display student information.
3. **Update:** Modify existing student details.
4. **Delete:** Remove student records.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd Student-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Key Learnings

Through this project, I gained practical experience in:

- Building web applications using FastAPI.
- Connecting Python applications with SQLite.
- Performing database operations using SQL queries.
- Handling HTML form submissions.
- Validating input data using Pydantic.
- Rendering dynamic web pages using Jinja2.
- Implementing complete CRUD functionality.

## Acknowledgements

Special thanks to **Innomatics Research Labs** and **Full Stack Experts Academy** for their guidance and support throughout my learning journey.

---

**Developed as part of my Python Full Stack Development learning journey.** 🚀
