''' Q11'''


import pandas as pd

df = pd.read_csv("../Data/pokemon.csv")

df = df.identifier.str.split('-', expand=True)[0].drop_duplicates()

df.to_csv('q11.out', index=False)