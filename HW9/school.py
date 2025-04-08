# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 12:46:08 2025

@author: lhmaj
"""
from flask import Flask, jsonify, request
import sqlite3, init_db


db = 'data/school.db'

init_db.init_db()

createStudent = "CREATE TABLE IF NOT EXISTS STUDENT (ID integer, name text, email text, phone integer, year integer, status text);"
createTeacher = "CREATE TABLE IF NOT EXISTS TEACHER (ID integer, name text, email text, phone integer);"
createClass = "CREATE TABLE IF NOT EXISTS CLASS (ID integer, name text, teacherID integer, department text);"

app = Flask(__name__)

countclasses = []
teachers = []
students = []
#EX STUDENT : {"ID":"1","name":"1","email":"1","phone":"1","year":"1","status":"1"}
#EX TEACHER: {"ID":"1","name":"1","email":"1","phone":"1"}
#EX CLASS: {"name":"1","ID":"1","teacherID":"1"}




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#--Student
@app.route('/student', methods=['POST', 'GET', 'DELETE'])
def student():
    data = request.get_json()
#make sure there's data    
    if not data:
            return jsonify({'error': 'Need data'}), 500
#post....    
    if request.method == 'POST':
#make sure required fields, if not, return error of what field needed        
        required_fields = ['ID', 'name', 'email', 'phone', 'year', 'status']
        for field in required_fields:
            if not data.get(field):  
                return jsonify({'error': f'{field} is required'}),500
       
#set up variables for json info
        pID = data.get("ID")
        pname = data.get('name')
        pemail = data.get('email')
        pphone = data.get('phone')
        pyear = data.get('year')
        pstatus = data.get('status')
        
        
#insert json values into database         
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
            c.execute(createStudent)
            q = "INSERT INTO STUDENT(id,name,email,phone,year,status) VALUES('{i}','{n}','{e}','{p}','{y}','{s}')".format(i=pID,n=pname,e=pemail,p=pphone,y=pyear,s=pstatus)
            c.execute(q)
            conn.commit()
            conn.close()
            return jsonify({'Added Student With ID': data["ID"]})
        except Exception as e:
            print(e)
            return jsonify("{'error':'student post'}"),500
    
######################################################
    if request.method == 'DELETE':
        deleteMe = data.get('ID')
        if deleteMe is None:
            return jsonify({'error': 'Enter student ID to delete student'}), 400
    
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
    
            c.execute("SELECT * FROM STUDENT WHERE ID = ?", (deleteMe,))
            student = c.fetchone()
            if not student:
                return jsonify({'error': f"No student found with ID {deleteMe}"}), 404
    
            c.execute("DELETE FROM STUDENT WHERE ID = ?", (deleteMe,))
            conn.commit()
            conn.close()
            
            
            #without global I kept appending to the list over and over and over
            global students
            students = [s for s in students if s.get("ID") != deleteMe]
    
            return jsonify({"Deleted Student with ID": deleteMe})
        except Exception as e:
            print("Delete error:", e)
            return jsonify({'error': 'student delete'}), 500
# ######################################################    
    if request.method == 'GET':
        getMe = data.get('ID')
        if getMe is None:
            return jsonify({'error': 'Enter student ID to get student info'}), 400
    
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
    
            c.execute("SELECT * FROM STUDENT WHERE ID = ?", (getMe,))
            rows = c.fetchall()
            conn.close()
    
            # Clear the list before appending
            students.clear()
    
            for row in rows:
                student = {
                    "ID": row[0],
                    "name": row[1],
                    "email": row[2],
                    "phone": row[3],
                    "year": row[4],
                    "status": row[5]
                }
                students.append(student)
    
            if len(students) == 0:
                return jsonify({"error": f"No student with ID {getMe} found."})
    
            return jsonify({"STUDENT": students})
    
        except Exception as e:
            print("broken", e)
            return jsonify({'error': 'student get error'}), 500
                

@app.route('/student/phone', methods=['POST'])
def student_phone():
    
    SID = request.args.get('ID')
    NewPhone = request.args.get('phone')
    if SID == None:
        return 'jsonify({"error":"Please enter query parameter for student ID to continue"})'
    
    if NewPhone == None:
        return 'jsonify({"error":"Please enter query parameter for student phone to continue"})'
        
    try:
       conn = sqlite3.connect(db)
       conn.row_factory = sqlite3.Row
       c = conn.cursor()

       # Check if student exists
       c.execute("SELECT phone FROM STUDENT WHERE ID = ?", (SID,))
       student = c.fetchone()
       
       if student is None:
           return jsonify({"error": f"No student found with ID {SID}"}), 404

       OldPhone = student["phone"]

       # Update phone number
       c.execute("UPDATE STUDENT SET phone = ? WHERE ID = ?", (NewPhone, SID))
       conn.commit()

       return jsonify({f"Updated phone for Student {SID}": {"old": OldPhone, "new": NewPhone}}), 200

    except Exception as e:
       print(e)
       return jsonify({"error": "Something went wrong"}), 500

    finally:
       conn.close()
            
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






    
# ##--Teacher    
@app.route('/teacher', methods=['POST', 'GET', 'DELETE'])
def teacher():
    data = request.get_json()
    
    if not data:
            return jsonify({'error': 'Need data'}), 500
    
    if request.method == 'POST':
        required_fields = ['ID', 'name', 'email', 'phone']               
        for field in required_fields:
            if not data.get(field):  
                return jsonify({'error': f'{field} is required'}),500
     
        pID = data.get("ID")
        pname = data.get('name')
        pemail = data.get('email')
        pphone = data.get('phone')
        
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
            c.execute(createTeacher)
            q = "INSERT INTO TEACHER(id,name,email,phone) VALUES('{i}','{n}','{e}','{p}')".format(i=pID,n=pname,e=pemail,p=pphone)
            c.execute(q)
            conn.commit()
            conn.close()
            return jsonify({'Added Teacher With ID': data["ID"]})
        except Exception as e:
            print(e)
            return jsonify("{'error':'teacher post'}"),500
    
# ######################################################
    if request.method == 'DELETE':
        required_fields = ['ID']
        
        deleteMe = data.get('ID')
        
        if data.get('ID') is None:
            return 'Enter teacher ID to delete teacher'
        
        deleteTeacher = f"DELETE FROM TEACHER WHERE ID = {deleteMe};"
        
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
            print(deleteTeacher)
            c.execute(deleteTeacher)
            conn.commit()
            rows = c.fetchall()
            conn.close()
            global teachers
            teachers = [t for t in teachers if t["ID"] != deleteMe]
            return jsonify({"Deleted Teacher with ID": deleteMe})
        except Exception as e:
            print(e)
            return jsonify("{'error':'teacher delete'}"),500
          
# ######################################################    
    if request.method == 'GET':
        getMe = data.get('ID')
        
        # Check if ID was provided
        if getMe is None:
            return jsonify({'error': 'Enter teacher ID to get teacher info'}), 400
        
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
        
            # Use parameterized query for safety
            c.execute("SELECT * FROM TEACHER WHERE ID = ?", (getMe,))
            rows = c.fetchall()
            conn.close()
        
            # If no teacher is found, return an error
            if len(rows) == 0:
                return jsonify({"error": f"No teacher with ID {getMe} found."}), 404
            
            # Prepare teacher data
            teacher = {
                "ID": rows[0][0],
                "name": rows[0][1],
                "email": rows[0][2],
                "phone": rows[0][3],
            }
    
            return jsonify({"TEACHER": teacher}), 200
    
        except Exception as e:
            print("Error:", e)
            return jsonify({"error": "Teacher get error"}), 500
            
@app.route('/teacher/<ID>', methods=['GET'])
def teacherid(ID):
    if ID is None:
        return jsonify({"error":"teacher with this ID not found."})
    
    find = f"SELECT * FROM CLASS where teacherID = {ID}"
    
    try:
        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(find)
        rows = c.fetchall()
        if not rows:
            return jsonify({"error": "No classes for this teacher yet"})
        conn.close()
        TD = []
        for row in rows:
            TD.append(dict(row))
        return jsonify({
            f"Teacher {ID} Class Count": len(TD),
            f"Teacher {ID} Classes": TD
            })    
    except Exception as e:
        print("broken",e)

@app.route('/teacher/phone', methods=['POST'])
def teacher_phone():
    
    TID = request.args.get('ID')
    NewPhone = request.args.get('phone')
    if TID == None:
        return 'jsonify({"error":"Please enter query parameter for teacher ID to continue"})'
    
    if NewPhone == None:
        return 'jsonify({"error":"Please enter query parameter for teacher phone to continue"})'
        
    try:
       conn = sqlite3.connect(db)
       conn.row_factory = sqlite3.Row
       c = conn.cursor()

       # Check if student exists
       c.execute("SELECT phone FROM TEACHER WHERE ID = ?", (TID,))
       teacher = c.fetchone()
       
       if teacher is None:
           return jsonify({"error": f"No teacher found with ID {TID}"}), 404

       OldPhone = teacher["phone"]

       # Update phone number
       c.execute("UPDATE TEACHER SET phone = ? WHERE ID = ?", (NewPhone, TID))
       conn.commit()

       return jsonify({f"Updated phone for Teacher {TID}": {"old": OldPhone, "new": NewPhone}}), 200

    except Exception as e:
       print(e)
       return jsonify({"error": "Something went wrong"}), 500

    finally:
       conn.close()        
    
                
          

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    

# ##--Class
@app.route('/class', methods=['POST', 'GET', 'DELETE'])
def classs():
    data = request.get_json()
    
    
    if not data:
            return jsonify({'error': 'Need data'}), 500
    
    if request.method == 'POST':
        required_fields = ['ID', 'name', 'teacherID']
        
        data['department'] = data.get('department', 'Misc')        
       
        for field in required_fields:
            if not data.get(field):  
                return jsonify({'error': f'{field} is required'}),500
        
        
        countclasses.append(data)
       
        pID = data.get("ID")
        pname = data.get('name')
        pteacherID = data.get('teacherID')
        pdepartment = data.get('department')
        
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
            c.execute(createClass)
            q = "INSERT INTO CLASS(id,name,teacherID,department) VALUES('{i}','{n}','{t}','{d}')".format(i=pID,n=pname,t=pteacherID,d=pdepartment)
            c.execute(q)
            conn.commit()
            conn.close()
            
            return jsonify({'Added Class With ID': data["ID"]})
        except Exception as e:
            print(e)
            return jsonify("{'error':'class post'}"),500
    
# ######################################################
    if request.method == 'DELETE':
        
        deleteMe = request.args.get('ID')
        
        if deleteMe == None:
            return jsonify({"error":"need query data"})
        
        for c in countclasses:
            if c['ID'] == deleteMe:
                countclasses[:] = [ c for c in countclasses if c.get('ID') != deleteMe]
        
        deleteClass = f"DELETE FROM CLASS WHERE ID = {deleteMe};"
        
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
            print(deleteClass)
            c.execute(deleteClass)
            conn.commit()
            testData = "SELECT * FROM CLASS"
            c.execute(testData)
            rows = c.fetchall()
            conn.close()
            for row in rows:
                print(row)
            return jsonify({"Deleted Class with ID": deleteMe})
        except Exception as e:
            print(e)
            return jsonify("{'error':'class delete'}"),500
# ######################################################       
    if request.method == 'GET':
            if request.args.get('count') == 'true':
                return jsonify({'count': len(countclasses)})
            
            classes = []
            required_fields = ['ID']
            getMe = data.get('ID')
            getData = f"SELECT * FROM CLASS WHERE ID = {getMe}"

            if data.get('ID') is None:
                return 'Enter class ID to get student info'
            
            try:
                conn = sqlite3.connect(db)
                c = conn.cursor()
                c.execute(getData)
                rows = c.fetchall()
                conn.close()
                for row in rows:
                    classs = {
                        "ID": row[0],
                        "name": row[1],
                        "teacherID": row[2],
                        "department": row[3]
                        }
                    classes.append(classs)
                if len(classes) == 0:
                    return jsonify({"error":f"no class with ID {getMe} found. "})
                return jsonify({"CLASSES": classes})
            except Exception as e:
                print("broken",e)
                return"boo"
        
            
        
        

        
        
    





app.run(host='0.0.0.0', port=9998, debug=False)
