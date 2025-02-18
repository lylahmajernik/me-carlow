'''
q8
'''

import pandas as pd

p = pd.read_csv("../Data/pokemon.csv")

pt = pd.read_csv("../Data/pokemon_types.csv")

t = pd.read_csv("../Data/types.csv")

ppt = p.merge(pt, how='left',left_on="id",right_on="pokemon_id", suffixes =("_pokemon","_poketypes"))
df = ppt.merge(t, how='left',left_on="type_id", right_on="id", suffixes =('_pokemon','_types'))
del(p)
del(pt)
del(t)
del(ppt) 

df = df[(df['identifier_types'] != 'fire')]

remaining = df.count()['identifier_pokemon'].astype(str)

file = open('q8.out','w')
file.write("remaining pokemon: " + remaining)
file.close()

