# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3
import shutil


shutil.copy('../Q2/poke2.db', './poke4.db')

df = pd.read_csv('../data/pokemon.csv')
df1 = pd.read_csv('../data/pokemon_types.csv')
df2 = pd.read_csv('../data/pokemon_type_names.csv')



db = 'poke4.db'


df = df[['id','identifier','height','weight','base_experience']].drop_duplicates()
df2 = df2[df2['local_language_id'] == 9]   




try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS POKEMON\
                   (ID          INTEGER     PRIMARY KEY,\
                    name        TEXT        NOT NULL UNIQUE,\
                    height      INTEGER,\
                    weight      INTEGER,\
                    baseXP      INTEGER)'
                       );
    for index, row in df.iterrows():
        c.execute("INSERT OR IGNORE INTO POKEMON (ID,name,height,weight,baseXP)\
                       VALUES (?,?,?,?,?)",\
                    (row['id'],row['identifier'],row['height'],row['weight'],row['base_experience']))
    conn.commit()
    conn.close()
    print('success q 4 table pokemon')
except Exception as e:
    print('failure', e)
try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS POKEMON_TYPES\
                   (ID      INTEGER,\
                    name    TEXT)'
                       );
    for index, row in df2.iterrows():
        c.execute("INSERT INTO POKEMON_TYPES (ID,name)\
                       VALUES (?,?)",\
                    (row['type_id'],row['name']))
    conn.commit()
    conn.close()
    print('success q 4 table pokemon_types')
except Exception as e:
    print('failure', e)