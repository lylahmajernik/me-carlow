"""
Q10
Lylah Majernik
HW3
"""

import pandas as pd

dfR = pd.read_csv("../data/regions.csv")
dfL = pd.read_csv("../data/locations-2.csv")

region = str(input("Type region you'd like to search\n"))

if region not in dfR['identifier'].values:
    print("This region does not exist")
else:
    match = dfR['identifier']==region
    ##I honestly do not fully understand how this next line works but after many tries it is how I got it.
    ##specifically I don't understand what values[0] means?
    idnum = (dfR.loc[match, 'id'].values[0])
    print(f"This region's id is: {idnum}")
    locationCount = 0
    for index, row in dfL.iterrows():
        
        if row['region_id'] == idnum:
            locationCount += 1
    print(f"There are {locationCount} locations in {region}.")

