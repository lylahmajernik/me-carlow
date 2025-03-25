# -*- coding: utf-8 -*-
"""
HW 7 Q1 MAJERNIK
"""

from flask import Flask
import pandas as pd

df = pd.read_csv('../data/pokemon.csv')
print(df.head())

app = Flask(__name__)

@app.route('/')
def hello():
    poke = df['identifier'].sample(1).values[0]
    return f'Hello, {poke.title()}!'


app.run(host='0.0.0.0', port=5690, debug=False)