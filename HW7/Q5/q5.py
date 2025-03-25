# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 15:57:24 2025

@author: lhmaj
"""

#I understand I porbably shouldn't have
#put GET on all of them but 
#curl -X POST http://localhost:8989/create

from flask import Flask, request
import pandas as pd

df = pd.read_csv('../data/pokemon.csv')

app = Flask(__name__)


team = []
#Post -> Build
#Get -> Show
#Del -> Del
@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        if len(team) == 0:
            randomTeam = df.sample(6)['identifier']
            for i in randomTeam:
                team.append(i)
            return team 
        else:
            return 'Team already exists. Please delete existing team to create new one.'
    else:
        return 'To generate team, you must send POST request'
@app.route('/list', methods=['GET'])
def list():
    if len(team) > 0:
        return team
    else:
        return 'No team exists.'

@app.route('/delete', methods=['GET','DELETE'])
def delete():
    if request.method == 'DELETE':
        team.clear()
        return 'Team deleted'
    else:
        return 'To delete team, you must send DELETE request'
        
    
    



app.run(host='0.0.0.0', port=8989, debug=False)
    
