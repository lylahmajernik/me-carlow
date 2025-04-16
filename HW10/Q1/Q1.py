# -*- coding: utf-8 -*-
"""Q1 HW 10 Majernik"""
import sqlite3

db = 'poke1.db'

try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS POKEMON\
                   (ID      INTEGER      PRIMARY KEY,\
                    name    TEXT         NOT NULL UNIQUE,\
                    height  INTEGER,\
                    weight  INTEGER,\
                    baseXP  INTEGER)STRICT'
                       );
    conn.commit()
    conn.close()
    print('success Q1')
except:
    print('failure')
  
                   

