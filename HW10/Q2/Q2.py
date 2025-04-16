# -*- coding: utf-8 -*-
"""Q2 HW 10 Majernik"""


import sqlite3
import pandas as pd
import shutil


shutil.copy('../Q1/poke1.db', './poke2.db')

df = pd.read_csv('../data/pokemon.csv')

db = 'poke2.db'

df = df[['id','identifier','height','weight','base_experience']].drop_duplicates()
    




try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS POKEMON\
                   (ID INTEGER PRIMARY KEY,\
                    name TEXT NOT NULL UNIQUE,\
                    height INTEGER,\
                    weight INTEGER,\
                    baseXP INTEGER)'
                       );
    for index, row in df.iterrows():
        c.execute("INSERT OR IGNORE INTO POKEMON (ID,name,height,weight,baseXP)\
                       VALUES (?,?,?,?,?)",\
                    (row['id'],row['identifier'],row['height'],row['weight'],row['base_experience']))
    
  
    conn.commit()
    conn.close()
    print('success q2')
except Exception as e:
    print('failure', e)

