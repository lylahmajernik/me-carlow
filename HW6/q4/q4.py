""" Majernik Q4
- same as before
- min strength
- max strength
- level
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
e = pd.read_csv("../data/experience.csv")

df = ty.merge(t2, how="left", left_on="id", right_on="type_id", suffixes=("_type","_poke"))
df = df.merge(s, how='left',left_on='pokemon_id',right_on='id', suffixes=("","_species"))
df = df.merge(g, how='left', left_on='generation_id_species',right_on='id', suffixes=("","_gen"))
df = df.merge(p, how='left',left_on='id_species', right_on='id', suffixes=("","_poke"))
df = df.merge(e, how ='left',left_on='growth_rate_id', right_on='growth_rate_id', suffixes=("","_exp"))

del ty, t2, s, g, p, e


df = df.rename(columns ={'identifier_species':'poke_identifier','id_species':'poke_id','identifier':'type_identifier','id_gen':'id_gen','identifier_gen':'generation'})
df = df[['poke_identifier','poke_id','type_id','type_identifier','id_gen','generation','height','weight','base_experience','level','experience','growth_rate_id']]
df = df.assign(strength = lambda x: ( (x['height']*5) + (x['weight']*2) + x['experience']))

while True:
    search = str(input("Enter the Pokemon Type you would like to search...\n")).lower()
    if search not in df['type_identifier'].values:
         print("\nI don't know that Pokemon type...\n\n")
         continue
    dfmean = df[df['type_identifier'] == search].groupby('level')['strength'].mean().round(0).reset_index(name='avg_strength')
    dfmin = df[df['type_identifier'] == search].groupby('level')['strength'].min().round(0).reset_index(name='min_strength')
    dfmax = df[df['type_identifier'] == search].groupby('level')['strength'].max().round(0).reset_index(name='max_strength')
    del df
    df = dfmean.merge(dfmin, how='left',left_on='level', right_on='level')
    df = df.merge(dfmax, how='left',left_on='level', right_on='level')
    df['level'] = df['level'].astype(int)
    del dfmean, dfmin, dfmax
    b = df.plot(kind='line', x='level',y=['min_strength','avg_strength','max_strength'], color = ['grey','red','grey'],legend=True)
    plt.fill_between(df['level'], df['min_strength'], df['max_strength'], color='lightgrey', alpha=0.2)

    plt.ylabel('Strength (in 100,000s)')
    plt.xlabel('Level')
    plt.yticks(np.arange(0, max(df['max_strength']) + 100000, 100000))
    plt.xticks(np.arange(0, max(df['level'])+1, 10), rotation=0)
    
    plt.title(f'Strength Statistics of {search.title()} Pokemon by Level')
   
    plt.show()
    break
   
   