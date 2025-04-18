""" Majernik Q3 
height
weight 
base xp
type
generation

"""


import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt


ty = pd.read_csv("../data/types.csv")
t2 = pd.read_csv("../data/pokemon_types.csv")
s = pd.read_csv("../data/pokemon_species.csv")
g = pd.read_csv("../data/generations.csv")
p = pd.read_csv("../data/pokemon.csv")

typee = ty.merge(t2, how="left", left_on="id", right_on="type_id", suffixes=("_type","_poke"))
df1 = typee.merge(s, how='left',left_on='pokemon_id',right_on='id', suffixes=("","_species"))
df = df1.merge(g, how='left', left_on='generation_id_species',right_on='id', suffixes=("","_gen"))
df = df.merge(p, how='left',left_on='id_species', right_on='id', suffixes=("","_poke"))
  
del ty, t2, s, typee, df1, g, p
  
df = df.rename(columns ={'identifier_species':'poke_identifier','id_species':'poke_id','identifier':'type_identifier','id_gen':'id_gen','identifier_gen':'generation'})
df = df[['poke_identifier','poke_id','type_id','type_identifier','id_gen','generation','height','weight','base_experience']]
df = df.assign(strength = lambda x: ( (x['height']*5) + (x['weight']*2) + x['base_experience']))


while True:
    search = str(input("Enter the Pokemon Type you would like to search...\n")).lower()
    if search not in df['type_identifier'].values:
        print("\nI don't know that Pokemon type...\n\n")
        continue
    
    df = df[df['type_identifier'] == search].groupby('generation')['strength'].mean().round(0).reset_index(name='avg_strength')
    df['generation'] = df['generation'].apply(lambda x: x.replace("generation-", "").upper())
    b = df.plot(kind='line', x='generation',y='avg_strength',legend=False)
    plt.ylabel('Average Strength')
    plt.xlabel('Generation')
    plt.xticks(rotation=0)
    plt.title(f'Average Strength of {search.title()} Pokemon over each Generation')
    plt.show()
    break
    