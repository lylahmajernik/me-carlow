# -*- coding: utf-8 -*-
import pandas as pd
import shutil
import sqlite3

shutil.copy('../Q7/poke7.db', './poke9.db')

db = 'poke9.db'

try:
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT p.ID, p.name, p.height, p.weight, p.baseXP, t.name AS type_name\
                  FROM POKEMON p\
                  LEFT JOIN POKEMON_TYPES t ON p.type_id = t.ID')
    rows = c.fetchmany(10)
    for row in rows:
        print(f"{(row['name'].title())} - {row['type_name']}")    
    conn.commit()
    conn.close()
except Exception as e:
    print('Q9 failure',e)
    