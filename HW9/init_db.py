# -*- coding: utf-8 -*-
import sqlite3

db = 'data/school.db'

createStudent = "CREATE TABLE IF NOT EXISTS STUDENT (ID integer, name text, email text, phone integer, year integer, status text);"
createTeacher = "CREATE TABLE IF NOT EXISTS TEACHER (ID integer, name text, email text, phone integer);"
createClass = "CREATE TABLE IF NOT EXISTS CLASS (ID integer, name text, teacherID integer, department text);"

def init_db():

    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Create Students table
    cursor.execute(createStudent)

    # Create Courses table
    cursor.execute(createTeacher)

    # Create Enrollments table
    cursor.execute(createClass)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")