# -*- coding: utf-8 -*-
"""
Q12
Lylah Majernik
HW3
"""

import pandas as pd

dfR = pd.read_csv("../data/regions.csv")
dfL = pd.read_csv("../data/locations-2.csv")
dfP = pd.read_csv("../data/poke.csv")
loop = True 
print("Hello, Ash!")


while loop == True:
    menuSel = int(input("\n\n1. Search by Name\n2. Search by Region\n3. Exit\n"))
    if menuSel== 1:
        pokeName = str(input("Type the name of the pokemon you'd like to search.\n"))
        if pokeName not in dfP['identifier'].values:
            print("This Pokemon does not exist")
        else:
            found = dfP[dfP['identifier'] == pokeName]
            print(found)
    elif menuSel == 2:
         region = str(input("Type the region you'd like to search.\n"))
         if region not in dfR['identifier'].values:
             print("This region does not exist")
         else:
             match = dfR['identifier']==region
             idnum = (dfR.loc[match, 'id'].values[0])
             
             locs = dfL[dfL['region_id'] == idnum]
            
             print(locs['identifier'].to_string(index=False))
##I wasn't sure if you wanted us to remove index. 
         
    elif menuSel == 3:
        print("Goodbye")
        break
    else:
        print("Invalid input, try again.")
        continue