# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd


df2 = pd.read_csv('../data/pokemon_type_names.csv')
df2 = df2[df2['local_language_id'] == 9]

db = 'poke6.db'

q6b = 'CREATE TABLE IF NOT EXISTS POKEMON\
               (ID          INTEGER         PRIMARY KEY,\
                name        TEXT            NOT NULL UNIQUE,\
                height      INTEGER,\
                weight      INTEGER,\
                baseXP      INTEGER,\
                type_id     INTEGER         NOT NULL,\
                FOREIGN KEY(type_id) REFERENCES POKEMON_TYPES(ID))STRICT'

q6a = 'CREATE TABLE IF NOT EXISTS POKEMON_TYPES\
                (ID     INTEGER     PRIMARY KEY,\
                 name   TEXT        NOT NULL)'
                    
try:
    conn = sqlite3.connect(db, timeout=10.0)
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = 1')
    c.execute(q6a)
    print('success table pokemon Q6')
    c.execute(q6b)
    c.execute("INSERT OR IGNORE INTO POKEMON_TYPES (ID,name)\
                  VALUES (?,?)",\
                      (999,'UNKNOWN'))
    for index, row in df2.iterrows():
        c.execute("INSERT OR IGNORE INTO POKEMON_TYPES (ID,name)\
                       VALUES (?,?)",\
                    (row['type_id'],row['name']))
    conn.commit()
    conn.close()
    
    print('success table pokemon_types Q6')
except Exception as e:
    print('failure', e)