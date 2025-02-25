'''HW5 Q4 Majernik'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

colors = {}
col = pd.read_csv('../data/pokemon_colors.csv')
poke = pd.read_csv('../data/pokemon.csv')
spec = pd.read_csv('../data/pokemon_species.csv')

df = poke.merge(spec, how='left', left_on='identifier',right_on='identifier',suffixes=('','_species'))
df = df.merge(col, how='left', left_on='color_id', right_on='id', suffixes=("","color"))
del col, poke, spec

df = df[['identifier','base_experience','color_id','identifiercolor']]
df['identifier'] = df['identifier'].str.title()
colors = dict(zip(df['identifier'], df['identifiercolor']))

df = df.dropna().sample(10)


b = sns.barplot(data=df, x='identifier',y='base_experience', palette=colors, edgecolor='black')
b.set_xticklabels(b.get_xticklabels(),rotation=30) 
plt.xlabel('Name')
plt.ylabel('Base XP')
plt.title('Base XP of Pokemon')
plt.show()