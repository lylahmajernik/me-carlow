# -*- coding: utf-8 -*-
"""
HW7 Q6 Majenrik
"""

from flask import Flask, request
import pandas as pd

df = pd.read_csv('../data/pokemon.csv')

app = Flask(__name__)

file = open('out.log','w')
team = []
#Post -> Build
#Get -> Show
#Del -> Del

#Create
@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        if len(team) == 0:
            randomTeam = df.sample(6)['identifier']
            for i in randomTeam:
                team.append(i)
            file.write(f'CREATE - HTTP_POST - {team} added\n')
            return team 
        else:
            return 'Team already exists. Please delete existing team to create new one.'
    
    else:
        return 'To generate team, you must send POST request'

#List
@app.route('/list', methods=['GET'])
def list():
    if len(team) > 0:
        file.write(f'LIST - HTTP_GET - {team} listed\n')
        return team
    else:
        file.write('LIST - HTTP_GET - NO TEAM listed\n')
        return 'No team exists.'

#Delete
@app.route('/delete', methods=['GET','DELETE'])
def delete():
    if request.method == 'DELETE':
        file.write(f'DELETE - HTTP_DELETE - {team} deleted\n')
        team.clear()
        return 'Team deleted'
    else:
        return 'To delete team, you must send DELETE request'
        
    
    



app.run(host='0.0.0.0', port=8989, debug=False)
file.close() 