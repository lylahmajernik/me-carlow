'''HW5 Q8 Majernik'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('../data/pokemon_species.csv')
df2 = pd.read_csv('../data/pokemon.csv')

df = df.merge(df2, how='left', left_on='identifier', right_on='identifier', suffixes=('TYPE',""))
del df2

df = df[['identifier','is_legendary','is_mythical','base_experience','height','weight']].dropna()
df = df[(df.is_mythical == 1) | (df.is_legendary == 1)].sort_values(by='is_mythical')

df = df.assign(strength = lambda x: ((x['base_experience'] * 5) + ((x['height']*x['weight']) * 5)))
df['color'] = df.apply(lambda x: 'purple' if x['is_mythical'] == 1 
                       else 'gold' if x['is_legendary'] == 1 
                       else 'gray', axis=1)



df = df.sort_values(by='strength', ascending=False).head(5)
df['identifier'] = df['identifier'].str.title()
df.to_csv('q8.out')

b = sns.barplot(data=df, x='identifier',y='strength', palette=df['color'].tolist())
b.set_xticklabels(b.get_xticklabels(),rotation=30) 
plt.xlabel('Pokemon Name')
plt.ylabel('Strength(Millions)')
plt.title('Strongest Legendary & Mythical Pokemon')
plt.show()