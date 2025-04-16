# -*- coding: utf-8 -*-
"""Q3 HW 10 Majernik"""
import sqlite3
import pandas as pd
import shutil


shutil.copy('../Q2/poke2.db', './poke3.db')

db = 'poke3.db'


q3 = 'SELECT * FROM POKEMON WHERE ID > 0 AND ID < 36'
try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    c.execute(q3)
    rows = c.fetchall()
    for row in rows:
        print(f"{row['name']} - {row['id']}")
    conn.commit()
    conn.close()
    
except Exception as e:
    print('failure', e)

