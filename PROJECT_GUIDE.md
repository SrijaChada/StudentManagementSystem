# Student Management System - Complete Project Guide

## 📚 Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture & How It Works](#architecture--how-it-works)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Core Components Explained](#core-components-explained)
6. [Database Design](#database-design)
7. [Route Flow & How They Work](#route-flow--how-they-work)
8. [Frontend (Templates) Explained](#frontend-templates-explained)
9. [Advanced Concepts](#advanced-concepts)
10. [How to Run & Use](#how-to-run--use)

---

## Project Overview

### What is this project?
A **Student Management System** is a web application that allows administrators to:
- ✅ View all students in the database
- ✅ Add new student records
- ✅ Edit existing student information
- ✅ Delete student records
- ✅ Search students by name, roll number, or department

### Why is this useful?
Educational institutions need a centralized system to manage student data instead of using spreadsheets or manual records.

---

## Architecture & How It Works

### Basic Flow (Simple Version)

```
User Opens Browser
       ↓
Sends Request to http://127.0.0.1:5000
       ↓
Flask App Receives Request
       ↓
Python Code Processes Request (fetch data from database)
       ↓
HTML Template Renders with Data
       ↓
Browser Shows Beautiful Web Page
       ↓
User Interacts (clicks buttons, fills forms)
       ↓
Back to Step 2...
```

### Advanced Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                           │
│  (Your Web Browser - Chrome, Firefox, Edge, Safari)         │
│  - Displays HTML, CSS, JavaScript                           │
│  - User clicks buttons, fills forms                         │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP Request (GET/POST)
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                        │
│  (Flask Web Framework - Runs on Your Computer)              │
│  - app.py: Main application file                            │
│  - Routes: Handles /index, /student/add, /student/edit      │
│  - Views: Python functions that process requests            │
└──────────────────────┬──────────────────────────────────────┘
                       │ SQL Queries
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                    DATABASE LAYER                           │
│  (SQLite - Simple Database Engine)                          │
│  - students.db: File containing all student data            │
│  - Tables: 'students' table with rows & columns             │
└─────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

### What technologies are used?

| Technology | Purpose | Why? |
|-----------|---------|------|
| **Python** | Programming language | Easy, readable, powerful |
| **Flask** | Web framework | Lightweight, flexible, perfect for small/medium apps |
| **SQLite** | Database | Simple, no setup, stores data in single file |
| **HTML** | Structure | Defines page layout & elements |
| **CSS** | Styling | Makes pages look beautiful |
| **Bootstrap 5** | CSS Framework | Pre-made styles for professional look |
| **Font Awesome** | Icons | Beautiful icons for buttons & labels |
| **Jinja2** | Template Engine | Embeds Python in HTML to display dynamic data |

---

## Project Structure

```
StudentManagementSystem/
├── app.py                    # Main Flask application (core logic)
├── students.db               # SQLite database (data storage)
├── dump.sql                  # SQL backup of database
├── students.csv              # CSV export of student data
├── students_table.txt        # Human-readable student table
├── templates/                # Folder for HTML templates
│   ├── base.html            # Base template (header, navbar, styling)
│   ├── index.html           # Home page (student list)
│   ├── form.html            # Add/Edit student form
│   └── view.html            # View single student details
└── README.md                # Project documentation
```

### Why this structure?
- **Separation of Concerns**: Code, templates, and data are separate
- **Easy Maintenance**: Each file has one specific purpose
- **Scalability**: Easy to add new features

---

## Core Components Explained

### 1. **app.py** - The Heart of the Application

#### What it does?
`app.py` is the main Python file that:
- Creates the Flask app
- Defines database connection
- Handles all routes (URL paths)
- Processes form submissions
- Manages database queries

#### Key Sections Explained

```python
# ============ IMPORTS ============
from flask import Flask, render_template, request, redirect, url_for, flash
# These are libraries that Flask provides:
# - render_template: Display HTML files with Python data
# - request: Get data from user (forms, URL parameters)
# - redirect: Send user to different page
# - url_for: Generate URLs dynamically
# - flash: Show success/error messages

import sqlite3
# sqlite3: Python's library to work with SQLite database

from pathlib import Path
# pathlib: Handle file paths in a clean way
```

#### Database Setup

```python
APP_DIR = Path(__file__).parent
# __file__ = current file path (app.py)
# .parent = folder containing this file
# APP_DIR now points to project folder

DB_PATH = APP_DIR / "students.db"
# Database file location

app = Flask(__name__)
# Create Flask application instance
# __name__ = current module name

app.secret_key = "change_this_to_a_random_secret"
# Secret key for session security (encrypts data)
```

#### Database Connection Function

```python
def get_connection():
    conn = sqlite3.connect(str(DB_PATH))
    # Connect to database
    # sqlite3.connect() opens the .db file
    
    conn.row_factory = sqlite3.Row
    # Return rows as dictionary-like objects
    # Instead of tuples: (1, 'CS101', 'Asha')
    # We get: {'id': 1, 'roll': 'CS101', 'name': 'Asha'}
    
    return conn
```

**Why?** This function avoids repeating connection code. It's a **reusable helper**.

#### Database Initialization

```python
def init_db():
    if DB_PATH.exists():
        return  # Database already exists, don't recreate
    
    conn = get_connection()
    cur = conn.cursor()  # Cursor = tool to run SQL queries
    
    cur.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique ID (auto-increasing)
        roll TEXT UNIQUE NOT NULL,             # Roll number (unique, required)
        name TEXT NOT NULL,                    # Student name (required)
        department TEXT,                       # Department (optional)
        year INTEGER,                          # Year (1,2,3,4)
        email TEXT                             # Email (optional)
    );
    """)
    # CREATE TABLE: Create a new table if it doesn't exist
    
    sample = [
        ("CS101", "Asha Patel", "CSE", 3, "asha.patel@gmail.com"),
        ("CS102", "Rohit Kumar", "CSE", 2, "rohit.kumar@gmail.com"),
        # ... more students
    ]
    
    cur.executemany(
        "INSERT INTO students (roll, name, department, year, email) VALUES (?, ?, ?, ?, ?)",
        sample
    )
    # INSERT: Add data to table
    # ? = placeholder (prevents SQL injection - a security issue)
    
    conn.commit()  # Save changes to database
    conn.close()   # Close connection
```

---

### 2. **Routes** - How URLs Are Handled

Routes are URL paths that trigger Python functions.

#### Route 1: Home Page (`/`)

```python
@app.route("/")
def index():
    """Display list of all students"""
    
    q = request.args.get("q", "").strip()
    # Get search query from URL
    # Example: http://127.0.0.1:5000/?q=Asha
    # request.args: Get URL parameters (everything after ?)
    # .get("q", ""): Get parameter 'q', default to empty string
    # .strip(): Remove whitespace
    
    conn = get_connection()
    cur = conn.cursor()
    
    if q:  # If user searched something
        like = f"%{q}%"
        # SQL LIKE pattern: %keyword% matches keyword anywhere
        # Example: %Asha% matches "Asha Patel", "Asha", etc.
        
        cur.execute(
            """SELECT * FROM students 
               WHERE roll LIKE ? OR name LIKE ? OR department LIKE ? 
               ORDER BY id DESC""",
            (like, like, like)
        )
        # Search in 3 columns: roll, name, department
    else:  # No search, show all students
        cur.execute("SELECT * FROM students ORDER BY id DESC")
        # ORDER BY id DESC: Show newest students first
    
    rows = cur.fetchall()  # Get all matching rows
    conn.close()
    
    return render_template('index.html', students=rows)
    # Pass data to template
    # Template gets 'students' variable with all the rows
```

#### Route 2: Add Student (`/student/add`)

```python
@app.route("/student/add", methods=["GET", "POST"])
def add_student():
    """Add a new student"""
    
    if request.method == "POST":
        # User submitted the form
        
        roll = request.form["roll"].strip()
        # request.form: Get data from HTML form
        # form["roll"]: Get value of input field named 'roll'
        
        name = request.form["name"].strip()
        department = request.form["department"].strip()
        year = int(request.form["year"])  # Convert to integer
        email = request.form.get("email", "").strip()
        
        conn = get_connection()
        cur = conn.cursor()
        
        try:  # Try to add student
            cur.execute(
                "INSERT INTO students (roll, name, department, year, email) VALUES (?, ?, ?, ?, ?)",
                (roll, name, department, year, email)
            )
            # ? prevents SQL injection attacks
            conn.commit()
            
            flash("Student added successfully.")
            # flash(): Show success message to user
            
            return redirect(url_for("index"))
            # Redirect to home page after adding
            
        except sqlite3.Error as e:
            # If duplicate roll number or other error
            conn.rollback()  # Undo changes
            flash(f"Error adding student: {e}")
            
        finally:
            conn.close()
    
    # GET request (user just opened the form page)
    return render_template('form.html', action_url=url_for("add_student"), student=None)
```

#### Route 3: Edit Student (`/student/<int:student_id>/edit`)

```python
@app.route("/student/<int:student_id>/edit", methods=["GET", "POST"])
def edit_student(student_id):
    """Edit existing student"""
    
    # <int:student_id>: URL parameter
    # Example: /student/5/edit means student_id = 5
    
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cur.fetchone()  # Get one row
    
    if not student:
        conn.close()
        flash("Student not found.")
        return redirect(url_for("index"))
    
    if request.method == "POST":
        # Similar to add_student, but UPDATE instead of INSERT
        roll = request.form["roll"].strip()
        # ... get other fields ...
        
        cur.execute(
            "UPDATE students SET roll=?, name=?, department=?, year=?, email=? WHERE id = ?",
            (roll, name, department, year, email, student_id)
        )
        # UPDATE: Modify existing row where id matches
        
        conn.commit()
        flash("Student updated successfully.")
        return redirect(url_for("view_student", student_id=student_id))
    
    else:
        # GET request (just opened the form)
        conn.close()
        return render_template('form.html', 
                             action_url=url_for("edit_student", student_id=student_id), 
                             student=student)
```

#### Route 4: View Student (`/student/<int:student_id>`)

```python
@app.route("/student/<int:student_id>")
def view_student(student_id):
    """Display single student details"""
    
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cur.fetchone()
    conn.close()
    
    if not row:
        flash("Student not found.")
        return redirect(url_for("index"))
    
    return render_template('view.html', student=row)
```

#### Route 5: Delete Student (`/student/<int:student_id>/delete`)

```python
@app.route("/student/<int:student_id>/delete")
def delete_student(student_id):
    """Delete a student"""
    
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    # DELETE: Remove row matching the id
    
    conn.commit()
    conn.close()
    
    flash("Student deleted.")
    return redirect(url_for("index"))
```

---

## Database Design

### SQLite Table Structure

```
TABLE: students
┌────┬────────┬──────────────┬────────────┬──────┬────────────────────────┐
│ id │ roll   │ name         │ department │ year │ email                  │
├────┼────────┼──────────────┼────────────┼──────┼────────────────────────┤
│ 1  │ CS101  │ Asha Patel   │ CSE        │ 3    │ asha.patel@gmail.com   │
│ 2  │ CS102  │ Rohit Kumar  │ CSE        │ 2    │ rohit.kumar@gmail.com  │
│ 3  │ EC201  │ Priya Singh  │ ECE        │ 4    │ priya.singh@gmail.com  │
│ 4  │ ME301  │ Vikram Sharma│ ME         │ 1    │ vikram.sharma@gmail.com│
│ 5  │ CS103  │ Anjali Verma │ CSE        │ 4    │ anjali.verma@gmail.com │
│ 6  │ EC202  │ Neha Singh   │ ECE        │ 3    │ neha.singh@gmail.com   │
└────┴────────┴──────────────┴────────────┴──────┴────────────────────────┘
```

### Column Explanation

| Column | Type | Purpose | Constraints |
|--------|------|---------|-------------|
| **id** | INTEGER | Unique identifier | PRIMARY KEY, AUTO INCREMENT |
| **roll** | TEXT | Roll number (CS101) | UNIQUE, NOT NULL |
| **name** | TEXT | Student's full name | NOT NULL |
| **department** | TEXT | CSE, ECE, ME, etc. | Optional |
| **year** | INTEGER | 1, 2, 3, or 4 | Optional |
| **email** | TEXT | Email address | Optional |

### Key Concepts

- **PRIMARY KEY**: Uniquely identifies each row (id)
- **UNIQUE**: roll number must be different for each student
- **NOT NULL**: Cannot be empty
- **AUTOINCREMENT**: Automatically increases id (1, 2, 3, ...)

---

## Route Flow & How They Work

### Complete User Journey

```
1. User opens browser → http://127.0.0.1:5000
   ↓
   @app.route("/") → index() function
   ↓
   Fetches all students from database
   ↓
   Returns render_template('index.html', students=rows)
   ↓
   Browser displays home page with student list

2. User clicks "Add Student" button
   ↓
   Button links to /student/add
   ↓
   @app.route("/student/add", methods=["GET", "POST"])
   ↓
   GET request: Displays empty form (form.html)
   
3. User fills form and clicks "Save Student"
   ↓
   POST request sends form data
   ↓
   add_student() processes data
   ↓
   Inserts new row into database
   ↓
   flash("Student added successfully.")
   ↓
   redirect(url_for("index")) → Back to home page

4. User clicks "View" button on a student
   ↓
   Links to /student/5 (example: id=5)
   ↓
   @app.route("/student/<int:student_id>")
   ↓
   Fetches that specific student from database
   ↓
   Returns view.html with student details

5. User clicks "Edit" button
   ↓
   Links to /student/5/edit
   ↓
   GET: Shows form pre-filled with current data
   POST: Updates database and redirects to view page

6. User clicks "Delete" button with confirmation
   ↓
   Links to /student/5/delete
   ↓
   Deletes row from database
   ↓
   Redirects to home page
```

---

## Frontend (Templates) Explained

### 1. **base.html** - Master Template

Think of it as a **template template**. All other templates inherit from it.

```html
<!doctype html>
<html>
  <head>
    <!-- CSS links for styling -->
    <link href="bootstrap@5.3.2">  <!-- Professional styles -->
    <link href="font-awesome">      <!-- Icons like ✏️, 🗑️, 👤 -->
    <style>
      /* Custom CSS for colors, fonts, spacing */
    </style>
  </head>
  <body>
    <nav>  <!-- Navigation bar at top -->
    </nav>
    
    <div class="container">
      <h1>Student Management System</h1>
      
      {% with messages = get_flashed_messages() %}
        {% if messages %}
          <!-- Show success/error messages -->
        {% endif %}
      {% endwith %}
      
      {% block content %}{% endblock %}
      <!-- Other templates insert their content here -->
      
      <footer><!-- Footer --></footer>
    </div>
  </body>
</html>
```

**Why inheritance?**
- Navbar, footer, styling appear on every page
- Only change the middle part (`{% block content %}`)
- DRY principle: Don't Repeat Yourself

### 2. **index.html** - Student List Page

```html
{% extends 'base.html' %}
{% block content %}

  <!-- Search Form -->
  <form method="get" action="{{ url_for('index') }}">
    <input name="q" placeholder="Search...">
    <button>Search</button>
  </form>
  <!-- Sends GET request with search query -->
  
  <!-- Add Button -->
  <a href="{{ url_for('add_student') }}">+ Add Student</a>
  
  <!-- Student Table -->
  <table>
    <thead>
      <tr>
        <th>Roll</th>
        <th>Name</th>
        <th>Department</th>
        <th>Year</th>
        <th>Email</th>
        <th>Actions</th>
      </tr>
    </thead>
    
    <tbody>
      {% for s in students %}
        <!-- Loop through each student -->
        <tr>
          <td>{{ s.roll }}</td>        <!-- Display roll number -->
          <td>{{ s.name }}</td>        <!-- Display name -->
          <td>{{ s.department }}</td>  <!-- Display department -->
          <td>{{ s.year }}</td>        <!-- Display year -->
          <td>{{ s.email }}</td>       <!-- Display email -->
          
          <td>
            <!-- Action Buttons -->
            <a href="{{ url_for('view_student', student_id=s.id) }}">View</a>
            <a href="{{ url_for('edit_student', student_id=s.id) }}">Edit</a>
            <a href="{{ url_for('delete_student', student_id=s.id) }}">Delete</a>
          </td>
        </tr>
      {% else %}
        <!-- If no students found -->
        <tr>
          <td colspan="6">No students found.</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>

{% endblock %}
```

**Key Jinja2 Concepts:**
- `{{ variable }}`: Display variable value
- `{% for %}...{% endfor %}`: Loop through items
- `{% if %}...{% endif %}`: Conditional display
- `{{ url_for('function_name') }}`: Generate URL for a route

### 3. **form.html** - Add/Edit Form

```html
{% extends 'base.html' %}
{% block content %}

<form method="post" action="{{ action_url }}">
  <!-- action_url changes based on add or edit -->
  <!-- For adding: /student/add -->
  <!-- For editing: /student/5/edit -->
  
  <label>Roll Number</label>
  <input type="text" name="roll" value="{{ student.roll if student else '' }}">
  <!-- If editing: show current roll number -->
  <!-- If adding: show empty field -->
  
  <label>Full Name</label>
  <input type="text" name="name" value="{{ student.name if student else '' }}">
  
  <label>Department</label>
  <input type="text" name="department" value="{{ student.department if student else '' }}">
  
  <label>Year</label>
  <select name="year">
    <option value="">Select year</option>
    {% for yr in [1,2,3,4] %}
      <option value="{{ yr }}" 
              {% if student.year|string == yr|string %}selected{% endif %}>
        Year {{ yr }}
      </option>
    {% endfor %}
  </select>
  
  <label>Email</label>
  <input type="email" name="email" value="{{ student.email if student else '' }}">
  
  <button type="submit">Save</button>
  <a href="{{ url_for('index') }}">Cancel</a>
</form>

{% endblock %}
```

### 4. **view.html** - Student Details Page

```html
{% extends 'base.html' %}
{% block content %}

<div>
  <label>Roll Number</label>
  <p>{{ student.roll }}</p>
  
  <label>Full Name</label>
  <p>{{ student.name }}</p>
  
  <!-- ... more fields ... -->
  
  <a href="{{ url_for('edit_student', student_id=student.id) }}">Edit</a>
  <a href="{{ url_for('index') }}">Back</a>
</div>

{% endblock %}
```

---

## Advanced Concepts

### 1. **SQL Injection Prevention**

```python
# ❌ VULNERABLE (DON'T DO THIS!)
query = f"SELECT * FROM students WHERE name = '{user_input}'"
cur.execute(query)

# ✅ SAFE (DO THIS!)
query = "SELECT * FROM students WHERE name = ?"
cur.execute(query, (user_input,))
```

**Why?** If user enters: `'; DROP TABLE students; --`
- Vulnerable version: Deletes entire table!
- Safe version: Treats it as a string value

### 2. **Request Methods**

- **GET**: Request data from server (URL parameters)
  - Example: `/index?q=Asha` (search)
  - Safe, cacheable, visible in URL

- **POST**: Send data to server (form data)
  - Example: Submit add/edit form
  - Secure, not visible in URL, modifies server state

### 3. **URL Generation with `url_for()`**

```python
# Instead of hardcoding URLs:
<a href="/student/5/edit">Edit</a>  # ❌ What if routes change?

# Use url_for:
<a href="{{ url_for('edit_student', student_id=5) }}">Edit</a>  # ✅ Dynamic
```

**Benefit**: If you change route from `/student/5/edit` to `/edit-student/5`, all URLs update automatically!

### 4. **Flash Messages**

```python
flash("Student added successfully.")
# Stores message in session
# Displays on next page load
# Automatically clears after display
```

### 5. **Template Inheritance**

```
base.html
  ├─ Common HTML (navbar, footer, styling)
  ├─ Placeholders {% block content %}
  
index.html extends base.html
  └─ Replaces {% block content %} with student list

form.html extends base.html
  └─ Replaces {% block content %} with form

view.html extends base.html
  └─ Replaces {% block content %} with student details
```

---

## How to Run & Use

### Starting the App

```powershell
# Method 1: Flask development server (has warning, that's OK)
python .\app.py

# Method 2: Waitress (no warning, production-ready)
pip install waitress
waitress-serve --port=5000 app:app
```

### Using the App

1. **View Students**: Open http://127.0.0.1:5000
2. **Search**: Enter name/roll/department in search box
3. **Add Student**: Click "+ Add Student" button, fill form, click "Save"
4. **View Details**: Click "View" button on any student
5. **Edit**: Click "Edit" button, modify data, click "Save"
6. **Delete**: Click "Delete" button (will ask confirmation)

---

## Complete Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│  BROWSER (Client)                                           │
│  User clicks "Add Student"                                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓ HTTP GET Request
                     
┌─────────────────────────────────────────────────────────────┐
│  FLASK SERVER (Server)                                      │
│  @app.route("/student/add", methods=["GET", "POST"])        │
│  if request.method == "GET":                                │
│      return render_template('form.html', ...)               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓ HTTP Response (HTML)
                     
┌─────────────────────────────────────────────────────────────┐
│  BROWSER                                                    │
│  Displays form with input fields                            │
│  User fills: Roll=CS104, Name=John, Dept=CSE, etc.         │
│  User clicks "Save Student"                                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓ HTTP POST Request (form data in body)
                     
┌─────────────────────────────────────────────────────────────┐
│  FLASK SERVER                                               │
│  if request.method == "POST":                               │
│      name = request.form["name"]  # Get "John"              │
│      ... get other fields ...                               │
│      INSERT INTO students VALUES (...)                      │
│      conn.commit()                                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓ HTTP Redirect (302) → /
                     
┌─────────────────────────────────────────────────────────────┐
│  BROWSER                                                    │
│  Redirects to home page                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓ HTTP GET Request /
                     
┌─────────────────────────────────────────────────────────────┐
│  FLASK SERVER                                               │
│  @app.route("/")                                            │
│  SELECT * FROM students                                     │
│  return render_template('index.html', students=rows)        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓ HTTP Response (HTML with new student)
                     
┌─────────────────────────────────────────────────────────────┐
│  BROWSER                                                    │
│  Displays updated student list including "John"             │
│  Shows: "Student added successfully." message               │
└─────────────────────────────────────────────────────────────┘
```

---

## Summary

### The 3-Layer Architecture Explained

1. **Presentation Layer** (Templates - HTML/CSS/JS)
   - What user sees and interacts with
   - Buttons, forms, tables, styling

2. **Application Layer** (Flask/Python - app.py)
   - Brain of the system
   - Routes, business logic, database queries
   - Connects presentation and data

3. **Data Layer** (SQLite - students.db)
   - Where data is stored
   - Tables, rows, columns
   - Persists information

Each layer communicates with others:
- Presentation sends requests to Application
- Application queries Data layer
- Application returns formatted data to Presentation

---

## Quick Reference

### Common SQL Queries Used

```sql
-- Get all students
SELECT * FROM students;

-- Get student by ID
SELECT * FROM students WHERE id = 1;

-- Add student
INSERT INTO students (roll, name, department, year, email) 
VALUES ('CS101', 'John', 'CSE', 3, 'john@gmail.com');

-- Update student
UPDATE students SET name='Jane', email='jane@gmail.com' WHERE id = 1;

-- Delete student
DELETE FROM students WHERE id = 1;

-- Search student
SELECT * FROM students WHERE name LIKE '%John%';

-- Count students
SELECT COUNT(*) FROM students;
```

### Common Flask Concepts

```python
@app.route("/path")                    # URL route
def function_name():                   # Handler function
    request.args.get()                 # GET parameters
    request.form[]                     # POST form data
    render_template()                  # Display HTML
    redirect(url_for())                # Go to another page
    flash()                            # Show message
```

---

## Questions to Test Your Understanding

1. Why do we use `{{ url_for() }}` instead of hardcoding URLs?
2. What's the difference between GET and POST requests?
3. Why is template inheritance useful?
4. How does SQL injection prevention work with `?` placeholders?
5. Explain the flow when user adds a new student.

---

**Happy Learning! 🎓**
