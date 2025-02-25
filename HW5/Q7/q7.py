'''HW5 Q7 Majernik MAYBEDONE?'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('../data/pokemon_species.csv')

df = df[['identifier','is_legendary','is_mythical']]
df = df[(df.is_mythical == 1) | (df.is_legendary == 1)].sort_values(by='is_mythical')

df.to_csv('q7.out')