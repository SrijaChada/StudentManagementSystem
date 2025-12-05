-- Student Management System Database Dump
-- Generated from students.db

CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        department TEXT,
        year INTEGER,
        email TEXT
    );

INSERT INTO students (id, roll, name, department, year, email) VALUES (1, 'CS101', 'Asha Patel', 'CSE', 3, 'asha.patel@gmail.com');
INSERT INTO students (id, roll, name, department, year, email) VALUES (2, 'CS102', 'Rohit Kumar', 'CSE', 2, 'rohit.kumar@gmail.com');
INSERT INTO students (id, roll, name, department, year, email) VALUES (3, 'EC201', 'Priya Singh', 'ECE', 4, 'priya.singh@gmail.com');
INSERT INTO students (id, roll, name, department, year, email) VALUES (4, 'ME301', 'Vikram Sharma', 'ME', 1, 'vikram.sharma@gmail.com');
INSERT INTO students (id, roll, name, department, year, email) VALUES (5, 'CS103', 'Anjali Verma', 'CSE', 4, 'anjali.verma@gmail.com');
INSERT INTO students (id, roll, name, department, year, email) VALUES (6, 'EC202', 'Neha Singh', 'ECE', 3, 'neha.singh@gmail.com');
