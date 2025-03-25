"""
HW 7 Q 4 Majenrik"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def sayhey():
    if request.method == 'POST':
        return "hello, CPU"
    else:
        return "hello, user"

#It returned hello, cpu in curl so I think that's how I check?
#C:\Users\lhmaj>curl -X POST http://localhost:4356/
#hello, CPU



app.run(host='0.0.0.0',port=4356,debug=False)

