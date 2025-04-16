# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd





df = pd.read_csv('../data/pokemon.csv')

db = 'poke10.db'

df = df[['id','identifier','height','weight','base_experience']].drop_duplicates()

df = df[(df['height'] >1) & (df['weight'] < 1000)]    
df = df.rename(columns={'id': 'ID'})
df = df.rename(columns={'identifier': 'name'})
df = df.rename(columns={'base_experience': 'baseXP'})

try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS POKEMON\
                   (ID      INTEGER     PRIMARY KEY,\
                    name    TEXT        NOT NULL UNIQUE,\
                    height  INTEGER     CHECK (height > 1),\
                    weight  INTEGER     CHECK (weight < 1000),\
                    baseXP  INTEGER)'
                );
    for index, row in df.iterrows():
            c.execute("""
                INSERT OR IGNORE INTO POKEMON (ID, name, height, weight, baseXP)
                VALUES (?, ?, ?, ?, ?)
            """, (
                row['ID'],
                row['name'],
                row['height'],
                row['weight'],
                row['baseXP']
            ))
    
    ID = int(input('Input pokemon ID (ID must be greater than 10194): '))
    name = input('Input pokemon name (must be unique): ')
    height = int(input('Input pokemon height (must be >1): '))
    weight = int(input('Input pokemon weight (must be < 1000): '))
    baseXP = int(input('Input pokemon base experience: '))
    
    c.execute('INSERT INTO POKEMON ( ID, name, height, weight, baseXP)\
              VALUES (?,?,?,?,?)',\
              (ID, name, height, weight, baseXP))
    conn.commit()
    conn.close()
    print(f"Pokemon Added to Database:\n \
        Name: {name}\n \
        ID: {ID}\n \
        Height: {height}\n \
        Weight: {weight}\n \
        Base XP: {baseXP}\n")
except Exception as e:
    print('Something went wrong:\n', e)