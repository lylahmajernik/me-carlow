"""
Q7
Lylah Majernik
HW3
"""

import pandas as pd

df = pd.read_csv("../data/poke.csv")

loop = True

columns = len(df.columns)
rows = len(df)
nameList = df.columns
nameList1 = nameList.tolist()
names = ', '.join(nameList1)

#Q7
search = str(input("Which pokemon would you like to search?\n"))

found = df[df.identifier.isin([search])]

if search not in df['identifier'].values:
    print("sorry, that pokemon does not exist.")
else:
    found = df[df.identifier.isin([search])]
    print(found)
    
   # -*- coding: utf-8 -*-

