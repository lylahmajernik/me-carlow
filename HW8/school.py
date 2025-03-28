# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, json

app = Flask(__name__)

# {
#   "ID": "12345",
#   "name": "jeff",
#   "email": "jeff@jeff.com",
#   "year": "2025",
#   "phone": "1112223333",
#   "status": "on"
# }



user_input = []

##--Student

@app.route('/student',methods=['POST','GET','DELETE'])
def student():
    data = request.get_json()
 #POST   
    if request.method == 'POST':
    #ID    
        if data.get('ID') is None:
            error_dict = dict(error='ID is required')
            return jsonify(error_dict),500
        # ID = data.get('ID')
        # return data.get('ID') 
    #Name    
        if data.get('name') is None:
            error_dict = dict(error='name is required')
            return jsonify(error_dict),500
        # return data.get('name')
        # name = data.get('name')
        
    #email
        if data.get('email') is None:
             error_dict = dict(error='email is required')
             return jsonify(error_dict),500
        # return data.get('email')
        # email = data.get('email')
    
    #phone
        if data.get('phone') is None:
             error_dict = dict(error='phone is required')
             return jsonify(error_dict),500
        # return data.get('phone')
        # phone = data.get('phone')
    
    #year
        if data.get('year') is None:
             error_dict = dict(error='year is required')
             return jsonify(error_dict),500
        # return data.get('year')
        # year = data.get('year')
    
    #status
        if data.get('status') is None:
              error_dict = dict(error='status is required')
              return jsonify(error_dict),500
        # return data.get('status')
        # status = data.get('status')
        
    keys = ['ID', 'name', 'email', 'year', 'phone', 'status']
    response = {key: data.get(key, 'N/A') for key in keys}
    return jsonify(response)

    # with open(student.csv, 'w') as f:
    #     json.dump(data,f,ident=2)
    
 #DELETE   
    if request.method == 'DELETE':
            data = request.get_json()
            
            student_id = data.get('ID')
            
            if not student_id:
                return jsonify({"error": "Not a valid ID"}), 400
            
            keys = ['ID', 'name', 'email', 'year', 'phone', 'status']
            response = {key: data.get(key, 'N/A') for key in keys}
            del response
            return f'student with id {student_id} has been deleted.'
           











    
# ##--Teacher    
# @app.route('/teacher',methods=['POST','GET','DELETE'])
# def teacher():
#     data = request.get_json()
#  #POST   
#     if request.method == 'POST':
#     #ID    
#         if data.get('ID') is None:
#             error_dict = dict(error='ID is required')
#             return jsonify(error_dict),500
#         return data.get('ID')  
#         ID = data.get('ID')
        
#     #Name    
#         if data.get('name') is None:
#             error_dict = dict(error='name is required')
#             return jsonify(error_dict),500
#         return data.get('name')
#         name = data.get('name')
        
#     #email
#         if data.get('email') is None:
#              error_dict = dict(error='email is required')
#              return jsonify(error_dict),500
#         return data.get('email')
#         name = data.get('email')
    
#     #phone
#         if data.get('phone') is None:
#              error_dict = dict(error='phone is required')
#              return jsonify(error_dict),500
#         return data.get('phone')
#         phone = data.get('phone')
        
# ##--Class
# @app.route('/class',methods=['POST','GET','DELETE'])
# def student():
#     data = request.get_json()
#  #POST   
#     if request.method == 'POST':
#     #ID    
#         if data.get('ID') is None:
#             error_dict = dict(error='ID is required')
#             return jsonify(error_dict),500
#         return data.get('ID')  
#         ID = data.get('ID')
        
#     #Name    
#         if data.get('name') is None:
#             error_dict = dict(error='name is required')
#             return jsonify(error_dict),500
#         return data.get('name')
#         name = data.get('name')
        
#     #department
#         if data.get('department') is None:
#              misc = dict(misc='Misc.')
#              return jsonify(misc)
#         return data.get('department')
#         department = data.get('department')
    
#     #teacherID
#         if data.get('teacherID') is None:
#              error_dict = dict(error='teacherID is required')
#              return jsonify(error_dict),500
#         return data.get('teacherID')
#         teacherID = data.get('teacherID')

app.run(host='0.0.0.0', port=9999, debug=False)


