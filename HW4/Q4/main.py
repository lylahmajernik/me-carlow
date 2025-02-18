# -*- coding: utf-8 -*-
"""
q4
"""

import pandas as pd

df = pd.read_csv("../Data/pokemon.csv")


dfP = df[df['identifier'].str.startswith('p')]

maxOrder = dfP['base_experience'].max()

dfOrder = dfP[dfP['base_experience'] == maxOrder]
dfOrder = dfOrder.sort_values('identifier', ascending=False)

dfOrder.to_csv('q4.out')