'''HW5 Q3 Majernik
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

enc = pd.read_csv('../data/encounters.csv')
poke = pd.read_csv('../data/pokemon.csv')
loc = pd.read_csv('../data/locations.csv')
reg = pd.read_csv('../data/regions.csv')

df = loc.merge(reg, how='left', left_on='region_id',right_on='id',suffixes=('L','R'))

df = df.merge(enc, how='left', left_on='idL',right_on='location_area_id', suffixes=("","E"))
del enc, poke, loc, reg

df['identifierR'] = df['identifierR'].str.title()
########### I couldn't get this to work with count()... WOuld return a series w count next to it but I wanted a df.
df = df.groupby('identifierR').size().reset_index(name='count')






b = sns.barplot(data=df, x='identifierR',y='count')
b.set_xticklabels(b.get_xticklabels(),rotation=30) 
plt.xlabel('Region Name')
plt.ylabel('# of Encounters')
plt.title('Pokemon Encounters by Region')
plt.show()
