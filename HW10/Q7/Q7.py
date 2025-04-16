# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 14:52:00 2025

@author: lhmaj
"""
import sqlite3
import pandas as pd
import shutil

df = pd.read_csv('../data/pokemon.csv')
df1 = pd.read_csv('../data/pokemon_types.csv')
df2 = pd.read_csv('../data/pokemon_type_names.csv')

df = df[['id','identifier','height','weight','base_experience']]
df1 = df1[['pokemon_id','type_id']]
df2 = df2[df2['local_language_id'] == 9][['type_id', 'name']]

df = df.merge(df1, how='left', left_on='id', right_on='pokemon_id').merge(df2, how='left', on='type_id')
del df1, df2

df['type_id'] = df['type_id'].fillna(999).astype(int)
df = df.drop(columns=['pokemon_id'])

shutil.copy('../Q6/poke6.db', './poke7.db')

db = 'poke7.db'

try:
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = 1')
    for index, row in df.iterrows():
            c.execute("""
                INSERT OR IGNORE INTO POKEMON (ID, name, height, weight, baseXP, type_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                row['id'],
                row['identifier'],
                row['height'],
                row['weight'],
                row['base_experience'],
                row['type_id']
            ))
    conn.commit()
    conn.close()
    print('success Q7')
    
except Exception as e:
    print('failure Q7', e)   
        