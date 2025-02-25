'''HW5 Q5 Majernik'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


colors = {}
df1 = pd.read_csv('../data/pokemon_types.csv')
df2 = pd.read_csv('../data/types.csv')


df = df1.merge(df2, how='left', left_on='type_id',right_on='id', suffixes=('POKE',""))
df = df[df['slot'] != 2]
del df1, df2 

df['type_color'] = df.apply(lambda x: 'white' if x['type_id'] == 1 
                       else 'firebrick' if x['type_id'] == 2  
                       else 'skyblue' if x['type_id'] == 3
                       else 'palegreen' if x['type_id'] == 4  
                       else 'saddlebrown' if x['type_id'] == 5 
                       else 'dimgrey' if x['type_id'] == 6
                       else 'olive' if x['type_id'] == 7
                       else 'lavender' if x['type_id'] == 8
                       else 'lightgrey' if x['type_id'] == 9
                       else 'orange' if x['type_id'] == 10
                       else 'turquoise' if x['type_id'] == 11
                       else 'yellowgreen' if x['type_id'] == 12
                       else 'gold' if x['type_id'] == 13
                       else 'bisque' if x['type_id'] == 14
                       else 'lightcyan' if x['type_id'] == 15
                       else 'hotpink' if x['type_id'] == 16
                       else 'indigo' if x['type_id'] == 17
                       else 'pink' if x['type_id'] == 18  
                       else 'gray', axis=1)
df = df.groupby(['type_id','identifier','type_color'])['type_id'].size().reset_index(name='count')

df.to_csv('q5.out')

b = sns.barplot(data=df, x='identifier',y='count', palette=df['type_color'].tolist(), edgecolor='black')
b.set_xticklabels(b.get_xticklabels(),rotation=30) 
plt.xlabel('Pokemon Type')
plt.ylabel('Count')
plt.title('# of Each Type of Pokemon')
plt.show()