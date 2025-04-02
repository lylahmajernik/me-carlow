# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, json

app = Flask(__name__)

fileS = open('data/student.csv', 'w')
fileT = open('data/teacher.csv', 'w')
fileC = open('data/class.csv', 'w')

students = []
teachers = []
classes = []

#EX STUDENT : {"ID":"1","name":"1","email":"1","phone":"1","year":"1","status":"1"}
#EX TEACHER: {"ID":"1","name":"1","email":"1","phone":"1"}
#EX CLASS: {"name":"1","ID":"1","teacherID":"1"}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##--Student
@app.route('/student', methods=['POST', 'GET', 'DELETE'])
def student():
    data = request.get_json()
    
    if not data:
            return jsonify({'error': 'Need data'}), 500
    
    if request.method == 'POST':
        required_fields = ['ID', 'name', 'email', 'phone', 'year', 'status']
               
        for field in required_fields:
            if not data.get(field):  
                return jsonify({'error': f'{field} is required'}),500
       
        students.append(data)
        
        open('data/student.csv','w')

        for s in students:      
            pretty = json.dumps(s, indent=4)
            with open('data/student.csv', 'a') as s:
                s.write(pretty + "\n\n")
        return jsonify({"Student Added":data})
    
######################################################
    if request.method == 'DELETE':
        required_fields = ['ID']
        
        deleteMe = data.get('ID')
        
        if data.get('ID') is None:
            return 'Enter student ID to delete student'
        
        for s in students:
            if s['ID'] == deleteMe:
                students[:] = [ s for s in students if s.get('ID') != deleteMe]
        
        open('data/student.csv','w')

        for s in students:      
            pretty = json.dumps(s, indent=4)
            with open('data/student.csv', 'a') as s:
                s.write(pretty + "\n\n")
            
        return f'Student with ID: {deleteMe} has been deleted.'
          
######################################################    
    if request.method == 'GET':
        required_fields = ['ID']
        
        getMe = data.get('ID')
        
        if data.get('ID') is None:
            return 'Enter student ID to get student info'
        
        for s in students:
            if s['ID'] == getMe:
                returnn = s
            
        return jsonify(returnn)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






    
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
       
        teachers.append(data)
        
        open('data/teacher.csv','w')

        for t in teachers:      
            pretty = json.dumps(t, indent=4)
            with open('data/teacher.csv', 'a') as t:
                t.write(pretty + "\n\n")
        return jsonify({"teacher Added":data})
    
######################################################
    if request.method == 'DELETE':
        required_fields = ['ID']
        
        deleteMe = data.get('ID')
        
        if data.get('ID') is None:
            return 'Enter teacher ID to delete teacher'
        
        for t in teachers:
            if t['ID'] == deleteMe:
                teachers[:] = [ t for t in teachers if t.get('ID') != deleteMe]
        
        open('data/teacher.csv','w')

        for t in teachers:      
            pretty = json.dumps(t, indent=4)
            with open('data/teacher.csv', 'a') as t:
                t.write(pretty + "\n\n")
            
        return f'teacher with ID: {deleteMe} has been deleted.'
          
######################################################    
    if request.method == 'GET':
            required_fields = ['ID']
            
            getMe = data.get('ID')
            
            if data.get('ID') is None:
                return 'Enter teacher ID to get teacher info'
            
            for t in teachers:
                if t['ID'] == getMe:
                    returnn = t
                
            return jsonify(returnn)
        
#Sorry I have to submit before I finish this part.        
@app.route('/teacher/<ID>', methods=['GET'])
def teacherid(ID):
    tid = []
    tid = [t for t in teachers if t['ID'] == ID]
    
    if len(tid) ==0:
        return jsonify({"error":"teacher with this ID not found."})
    
    if request.args.get('count') == 'true':
        i = 0
        for c in classes:
            if c['teacherID'] == ID:
                i+=1
              

        for t in teachers:
            if t['ID'] == ID:
                teacher['count'] = ('count', i) 
                returnnn = t
            
        return jsonify(returnnn)
                
          

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    

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
       
        classes.append(data)
        
        open('data/class.csv','w')

        for c in classes:      
            pretty = json.dumps(c, indent=4)
            with open('data/class.csv', 'a') as t:
                t.write(pretty + "\n\n")
        return jsonify({"Class Added":data})
    
######################################################
    if request.method == 'DELETE':
        
        deleteMe = request.args.get('ID')
        
        if deleteMe == None:
            return jsonify({"error":"need data"})
        for c in classes:
            if c['ID'] == deleteMe:
                classes[:] = [ c for c in classes if c.get('ID') != deleteMe]
        
        open('data/class.csv','w')

        for c in classes:      
            pretty = json.dumps(c, indent=4)
            with open('data/class.csv', 'a') as t:
                t.write(pretty + "\n\n")
            
        return f'class with ID: {deleteMe} has been deleted.'
######################################################       
    if request.method == 'GET':
            if request.args.get('count') == 'true':
                return jsonify({'count': len(classes)})
            else:
                required_fields = ['ID']
                
                getMe = data.get('ID')
                
                if data.get('ID') is None:
                    return 'Enter id to get class'
                
                for c in classes:
                    if c['ID'] == getMe:
                        returnn = c
                    
                return jsonify(returnn)
            
            
        
        

        
        
    





app.run(host='0.0.0.0', port=9999, debug=False)


