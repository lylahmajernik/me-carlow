''' Majernik Q2
-poke type
-pokemon type
-count of pokemon
-generation
'''

import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt


ty = pd.read_csv("../data/types.csv")
t2 = pd.read_csv("../data/pokemon_types.csv")
s = pd.read_csv("../data/pokemon_species.csv")
g = pd.read_csv("../data/generations.csv")

typee = ty.merge(t2, how="left", left_on="id", right_on="type_id", suffixes=("_type","_poke"))
df1 = typee.merge(s, how='left',left_on='pokemon_id',right_on='id', suffixes=("","_species"))
df = df1.merge(g, how='left', left_on='generation_id_species',right_on='id', suffixes=("","_gen"))
del ty, t2, s, typee, df1, g
    
df = df.rename(columns ={'identifier_species':'poke_identifier','id_species':'poke_id','identifier':'type_identifier','id_gen':'id_gen','identifier_gen':'generation'})
df = df[['poke_identifier','poke_id','type_id','type_identifier','id_gen','generation']]

while True:
    search = str(input("Enter the Pokemon Type you would like to search...\n")).lower()
    if search not in df['type_identifier'].values:
        print("\nI don't know that Pokemon type...\n\n")
        continue
    else:
        df = df[df['type_identifier'] == search].groupby('generation').size().reset_index(name='count')
        df['generation'] = df['generation'].apply(lambda x: x.replace("generation-", "").upper())
        b = df.plot(kind='bar', x='generation',y='count')
        plt.ylabel(f'Number of {search.title()} Pokemon')
        plt.xlabel('Generation')
        plt.xticks(rotation=0)
        plt.title(f'Number of {search.title()} Pokemon per Generation')
        break
    