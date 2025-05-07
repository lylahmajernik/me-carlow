# -*- coding: utf-8 -*-
"""
Lylah Majernik
Programming 2 Final
Submitted 5/7/2025
"""
import sqlite3
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename= '../teambattle.log', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')



df = pd.read_csv('../data/pokemon.csv')
df = df[['id','identifier','height','weight','base_experience']].drop_duplicates()
df = df.rename(columns={'id': 'ID', 'identifier': 'Name', 'height' : 'Height', 'weight' : 'Weight', 'base_experience':'Experience'})

db = ('../teambattle.db')

try:
    conn = sqlite3.connect(db)
    c = conn.cursor()
    with open('../sql/pokemon.sql', 'r') as file:
        pokemon = file.read()
    c.executescript(pokemon)
    df.to_sql(name='POKEMON', con=conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
    logger.info("pokemon.csv imported to pokemon.sql.")

except Exception as e:
    logger.error(f"Failure to import data: {e}")

del df 
