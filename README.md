# Student Management System (Simplified)

A **fresher-friendly full-stack Student Management System** built with **Flask, MySQL, HTML/CSS, and Bootstrap**.  
This project demonstrates CRUD operations, authentication, and basic web app design suitable for learning and showcasing on a resume.

---

## 🚀 Features

- **Authentication**
  - Admin login/logout
  - Passwords securely hashed using Werkzeug
- **Student Management**
  - Add, edit, delete, view students
  - Search students by name or roll number
- **Responsive UI**
  - Built with Bootstrap for mobile-friendly design
- **MySQL Integration**
  - Persistent storage for users and students

---

## 🗂️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** MySQL  
- **Authentication:** Werkzeug password hashing  

---

## 📂 Project Structure

student_management_simple/
│── app.py # Main Flask app
│── config.py # MySQL connection
│── requirements.txt # Python dependencies
│── templates/ # HTML templates (Jinja2)
│ ├── login.html
│ ├── students.html
│ ├── add_student.html
│ └── edit_student.html
└── db.sql # MySQL schema


---

## 🛠 Installation & Setup

1. **Clone the repository:**


git clone https://github.com/vishalbind-IT/student-management-system.git
cd student-management-system

## Create a virtual environment & install dependencies:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt


## Setup MySQL Database:

-- Run this in your MySQL console
SOURCE db.sql;


## Run the Flask App:

python app.py


## Open in Browser:

http://127.0.0.1:5000


## Default Admin Credentials:

Username: admin

Password: admin123

## 📌 Notes

For production, consider adding CSRF protection and stricter validation.

Use environment variables for sensitive credentials.

```bash
