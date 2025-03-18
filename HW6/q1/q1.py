# -*- coding: utf-8 -*-
"""
q1 Majernik
"""

import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt

ty = pd.read_csv("../data/types.csv")
t2 = pd.read_csv("../data/pokemon_types.csv")
s = pd.read_csv("../data/pokemon_species.csv")

typee = ty.merge(t2, how="left", left_on="id", right_on="type_id", suffixes=("_type","_poke"))
df = typee.merge(s, how='left',left_on='pokemon_id',right_on='id', suffixes=("","_species"))

del ty, t2, s, typee
    
df = df.rename(columns ={'identifier_species':'poke_identifier','id_species':'poke_id','identifier':'type_identifier'})
df = df[['poke_identifier','poke_id','type_id','type_identifier']]

df = df.groupby('type_identifier').size().reset_index(name='count').sort_values(by='count', ascending=True)

b = df.plot(kind='bar', x='type_identifier',y='count')
plt.ylabel('Number of Pokemon')
plt.xlabel('Type of Pokemon')
plt.title('Number of Each Type of Pokemon')