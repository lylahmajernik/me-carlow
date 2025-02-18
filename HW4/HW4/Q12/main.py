''' q12'''

import pandas as pd
df = pd.read_csv("../Data/pokemon.csv")

df.loc[df['identifier'].str.contains('-'), 'identifier'] = (
    df['identifier'].str.replace('-', ' ')
)

df['identifier'] = df['identifier'].str.title()

df.to_csv('q12.out')