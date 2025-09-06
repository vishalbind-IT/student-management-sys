from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from config import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("students"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            stored_password = user["password"]

            # Check if stored password is hashed
            if stored_password.startswith("pbkdf2:"):
                valid = check_password_hash(stored_password, password)
            else:
                valid = stored_password == password  # plain text fallback

            if valid:
                session["user"] = username
                return redirect(url_for("students"))

        flash("Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/students")
def students():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    search = request.args.get("search", "")

    if search:
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE %s OR roll_no LIKE %s",
            (f"%{search}%", f"%{search}%")
        )
    else:
        cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("students.html", students=students, search=search)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        roll_no = request.form["roll_no"]
        name = request.form["name"]
        email = request.form["email"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (roll_no, name, email) VALUES (%s, %s, %s)",
            (roll_no, name, email)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("students"))

    return render_template("add_student.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        roll_no = request.form["roll_no"]
        name = request.form["name"]
        email = request.form["email"]

        cursor.execute(
            "UPDATE students SET roll_no=%s, name=%s, email=%s WHERE id=%s",
            (roll_no, name, email, id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("students"))

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("edit_student.html", student=student)

@app.route("/delete/<int:id>")
def delete_student(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("students"))

if __name__ == "__main__":
    app.run(debug=True)
