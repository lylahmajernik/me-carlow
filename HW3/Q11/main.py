# -*- coding: utf-8 -*-
"""
Q11
Lylah Majernik
HW3
"""

import pandas as pd

dfR = pd.read_csv("../data/regions.csv")
dfL = pd.read_csv("../data/locations-2.csv")

noReg = []

print("Here is a list of locations not associated with a region:")

dfL['region_id'] = dfL['region_id'].fillna(value=0)

for index, row in dfL.iterrows():
      
    if row['region_id'] == 0:
        identifier = (row['identifier'])
        noReg.append(identifier)
i = 0
for loc in noReg:
    i += 1
    print(f"{i} - {loc}")


## It said list in the assignment so I took it literally and converted this into a list. 
    