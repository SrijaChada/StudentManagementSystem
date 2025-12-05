# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from sqlite3 import Error
from pathlib import Path


APP_DIR = Path(__file__).parent
DB_PATH = APP_DIR / "students.db"

app = Flask(__name__)
app.secret_key = "change_this_to_a_random_secret"

# HTML templates embedded as strings for single-file app
BASE_HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Student Management System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
      body { padding-top: 40px; }
      .container { max-width: 900px; }
      .table-fixed { table-layout: fixed; word-wrap: break-word; }
    </style>
  </head>
  <body>
    <div class="container">
      <h1 class="mb-4">Student Management System</h1>
      {% with messages = get_flashed_messages() %}
        {% if messages %}
          <div class="alert alert-success" role="alert">
            {{ messages[0] }}
          </div>
        {% endif %}
      {% endwith %}
      {% block content %}{% endblock %}
    </div>
  </body>
</html>
"""

INDEX_HTML = """
{% extends "base" %}
{% block content %}
  <div class="mb-3 d-flex justify-content-between">
    <form class="d-flex" method="get" action="{{ url_for('index') }}">
      <input class="form-control me-2" type="search" placeholder="Search by name, roll, or dept" aria-label="Search" name="q" value="{{ request.args.get('q','') }}">
      <button class="btn btn-outline-primary" type="submit">Search</button>
    </form>
    <a class="btn btn-primary" href="{{ url_for('add_student') }}">+ Add Student</a>
  </div>

  <table class="table table-striped table-fixed">
    <thead>
      <tr>
        <th style="width: 8%;">Roll</th>
        <th style="width: 24%;">Name</th>
        <th style="width: 18%;">Department</th>
        <th style="width: 12%;">Year</th>
        <th style="width: 18%;">Email</th>
        <th style="width: 20%;">Actions</th>
      </tr>
    </thead>
    <tbody>
      {% for s in students %}
      <tr>
        <td>{{ s.roll }}</td>
        <td>{{ s.name }}</td>
        <td>{{ s.department }}</td>
        <td>{{ s.year }}</td>
        <td>{{ s.email }}</td>
        <td>
          <a class="btn btn-sm btn-info" href="{{ url_for('view_student', student_id=s.id) }}">View</a>
          <a class="btn btn-sm btn-warning" href="{{ url_for('edit_student', student_id=s.id) }}">Edit</a>
          <a class="btn btn-sm btn-danger" href="{{ url_for('delete_student', student_id=s.id) }}" onclick="return confirm('Delete this student?');">Delete</a>
        </td>
      </tr>
      {% else %}
      <tr>
        <td colspan="6" class="text-center">No students found.</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
"""

FORM_HTML = """
{% extends "base" %}
{% block content %}
  <form method="post" action="{{ action_url }}">
    <div class="mb-3">
      <label class="form-label">Roll Number</label>
      <input type="text" class="form-control" name="roll" required value="{{ student.roll if student else '' }}">
    </div>
    <div class="mb-3">
      <label class="form-label">Full Name</label>
      <input type="text" class="form-control" name="name" required value="{{ student.name if student else '' }}">
    </div>
    <div class="mb-3">
      <label class="form-label">Department</label>
      <input type="text" class="form-control" name="department" required value="{{ student.department if student else '' }}">
    </div>
    <div class="mb-3">
      <label class="form-label">Year</label>
      <select class="form-select" name="year" required>
        {% set y = student.year if student else '' %}
        <option value="">Select year</option>
        {% for yr in [1,2,3,4] %}
          <option value="{{ yr }}" {% if y|string == yr|string %}selected{% endif %}>{{ yr }}</option>
        {% endfor %}
      </select>
    </div>
    <div class="mb-3">
      <label class="form-label">Email</label>
      <input type="email" class="form-control" name="email" value="{{ student.email if student else '' }}">
    </div>

    <button class="btn btn-primary" type="submit">Save</button>
    <a class="btn btn-secondary" href="{{ url_for('index') }}">Cancel</a>
  </form>
{% endblock %}
"""

VIEW_HTML = """
{% extends "base" %}
{% block content %}
  <dl class="row">
    <dt class="col-sm-3">Roll Number</dt><dd class="col-sm-9">{{ student.roll }}</dd>
    <dt class="col-sm-3">Full Name</dt><dd class="col-sm-9">{{ student.name }}</dd>
    <dt class="col-sm-3">Department</dt><dd class="col-sm-9">{{ student.department }}</dd>
    <dt class="col-sm-3">Year</dt><dd class="col-sm-9">{{ student.year }}</dd>
    <dt class="col-sm-3">Email</dt><dd class="col-sm-9">{{ student.email }}</dd>
  </dl>
  <a class="btn btn-warning" href="{{ url_for('edit_student', student_id=student.id) }}">Edit</a>
  <a class="btn btn-secondary" href="{{ url_for('index') }}">Back</a>
{% endblock %}
"""

# Utility: DB connection
def get_connection():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if DB_PATH.exists():
        return
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        department TEXT,
        year INTEGER,
        email TEXT
    );
    """)
    # Insert sample data
    sample = [
        ("CS101", "Asha Patel", "CSE", 3, "asha.patel@example.com"),
        ("CS102", "Rohit Kumar", "CSE", 2, "rohit.kumar@example.com"),
        ("EC201", "Priya Singh", "ECE", 4, "priya.singh@example.com")
    ]
    cur.executemany("INSERT INTO students (roll, name, department, year, email) VALUES (?, ?, ?, ?, ?)", sample)
    conn.commit()
    conn.close()
    print("Initialized DB at", DB_PATH)

# Routes
@app.route("/")
def index():
    q = request.args.get("q", "").strip()
    conn = get_connection()
    cur = conn.cursor()
    if q:
        like = f"%{q}%"
        cur.execute("SELECT * FROM students WHERE roll LIKE ? OR name LIKE ? OR department LIKE ? ORDER BY id DESC", (like, like, like))
    else:
        cur.execute("SELECT * FROM students ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', students=rows)

@app.route("/student/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        roll = request.form["roll"].strip()
        name = request.form["name"].strip()
        department = request.form["department"].strip()
        year = int(request.form["year"])
        email = request.form.get("email","").strip()
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO students (roll, name, department, year, email) VALUES (?, ?, ?, ?, ?)", (roll, name, department, year, email))
            conn.commit()
            flash("Student added successfully.")
            return redirect(url_for("index"))
        except Error as e:
            conn.rollback()
            flash(f"Error adding student: {e}")
        finally:
            conn.close()
    return render_template('form.html', action_url=url_for("add_student"), student=None)

@app.route("/student/<int:student_id>")
def view_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        flash("Student not found.")
        return redirect(url_for("index"))
    return render_template('view.html', student=row)

@app.route("/student/<int:student_id>/edit", methods=["GET", "POST"])
def edit_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cur.fetchone()
    if not student:
        conn.close()
        flash("Student not found.")
        return redirect(url_for("index"))

    if request.method == "POST":
        roll = request.form["roll"].strip()
        name = request.form["name"].strip()
        department = request.form["department"].strip()
        year = int(request.form["year"])
        email = request.form.get("email","").strip()
        try:
            cur.execute("UPDATE students SET roll=?, name=?, department=?, year=?, email=? WHERE id = ?",
                        (roll, name, department, year, email, student_id))
            conn.commit()
            flash("Student updated successfully.")
            return redirect(url_for("view_student", student_id=student_id))
        except Error as e:
            conn.rollback()
            flash(f"Error updating: {e}")
        finally:
            conn.close()
    else:
        conn.close()
        return render_template('form.html', action_url=url_for("edit_student", student_id=student_id), student=student)

@app.route("/student/<int:student_id>/delete")
def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    flash("Student deleted.")
    return redirect(url_for("index"))

# Register base template for render_template_string extends
@app.context_processor
def inject_base():
    return dict()

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
  app.run(debug=True)