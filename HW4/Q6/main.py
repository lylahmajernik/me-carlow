# -*- coding: utf-8 -*-
"""
q6 
"""
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

loop = True


while loop == True:
    poke = str(input("Enter a pokemon\n"))
    
    found = df[df.identifier_pokemon.isin([poke])]
    
    if poke not in df['identifier_pokemon'].values:
        print("sorry, that pokemon does not exist.")
    else:
            
    
        typedf = df[df.identifier_pokemon==poke]

        searchtype = typedf['identifier_types'].iloc[0]
        
        count = df.groupby('identifier_types').get_group(searchtype).count()['identifier_types'].astype(str)
        
        strongest = df.groupby('identifier_types').get_group(searchtype).sort_values(by='base_experience', ascending=False).head(1)['identifier_pokemon'].iloc[0]
        weakest = df.groupby('identifier_types').get_group(searchtype).sort_values(by='base_experience').head(1)['identifier_pokemon'].iloc[0]
        
        file = open('q6.out','w')
        file.write("type of pokemon: " + searchtype )
        file.write("\ncount of types: " + count)
        file.write("\nstrongest pokemon in this type: " + strongest)
        file.write('\nweakest pokemon in this type: ' + weakest)
        file.close()

        break



