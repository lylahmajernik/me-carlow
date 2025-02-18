# -*- coding: utf-8 -*-
"""
q7
"""

import pandas as pd

df = pd.read_csv("../Data/pokemon.csv")


df.loc[df['height']>100, 'identifier'] = df['identifier'].str.upper()
df.loc[(df['height'] >= 50) & (df['height'] <= 60), 'identifier'] = df['identifier'].str.title()
df.loc[df['height']<50, 'identifier'] = df['identifier'].str.lower()
   
df.to_csv('q7.out')