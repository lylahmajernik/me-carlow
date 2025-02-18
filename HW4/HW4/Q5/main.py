# -*- coding: utf-8 -*-
"""
q5
"""

import pandas as pd

df = pd.read_csv("../Data/pokemon.csv")

letters = str(input("What letters would you like to search?\n"))
dfP = df[df['identifier'].str.startswith(letters)]

maxOrder = dfP['base_experience'].max()

dfOrder = dfP[dfP['base_experience'] == maxOrder]
dfOrder = dfOrder.sort_values('identifier')

dfOrder.to_csv('q5.out')