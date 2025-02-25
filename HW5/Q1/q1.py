'''HW5 Q1 Majernik'''

import pandas as pd

df1 = pd.read_csv('../data/pokemon_species.csv')
df2 = pd.read_csv('../data/generations.csv')

df = df1.merge(df2, how='left',left_on='generation_id',right_on='id',suffixes=('_species','generations'))

df.to_csv('q1.out')

dfa = df[['identifier_species','generation_id']]
       
dfa.to_csv('q1.csv')     
