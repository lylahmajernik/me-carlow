'''HW5 Q6 Majernik'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df1 = pd.read_csv('../data/pokemon_types.csv')
df2 = pd.read_csv('../data/types.csv')

df = df1.merge(df2, how='left', left_on='type_id',right_on='id', suffixes=('POKE',""))
del df1, df2
df = df[df['slot'] == 2]
df = df.groupby('identifier').size().reset_index(name='count').sort_values(by='count', ascending = False).head(1)
typee = df['identifier'].iloc[0]
count = df['count'].iloc[0].astype(str)

file = open('q6.out','w')
file.write("Most common secondary type of pokemon\n")
file.write("type: " + typee)
file.write('\ncount: ' + count)
file.close()