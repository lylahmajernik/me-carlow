# -*- coding: utf-8 -*-
import sqlite3
import shutil


shutil.copy('../Q4/poke4.db', './poke5.db')

db = 'poke5.db'


q5 = 'DELETE FROM POKEMON WHERE ID > 10 OR weight < 30'

try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    c.execute(q5)
    rows = c.fetchall()
    for row in rows:
        print(row['name'],row['id'])
    conn.commit()
    conn.close()
    print('success q5')
except Exception as e:
    print('failure', e)