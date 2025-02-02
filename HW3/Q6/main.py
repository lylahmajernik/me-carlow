# -*- coding: utf-8 -*-
"""
Q6
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

#Q6

print(f"The pokemon dataset consts of {columns} columns and {rows} rows. It has the following column names: \n\n", names) 

print("\n\n")


