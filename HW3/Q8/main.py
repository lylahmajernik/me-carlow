# -*- coding: utf-8 -*-
"""
Q8
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
    
#Q8

    print("*************************************")
    searchNum = str(input("Enter a number\n"))
    
    if searchNum.isnumeric() == False:
        print("Invalid.")
        searchNum = str(input("Please enter a number\n"))
        if searchNum.isnumeric() == False:
            print("Error")
            loop == True
        else:
            num = int(searchNum)
            numid = df[(df['id'] ==num)]
            numindex = df[df.index==num]
            combined = pd.concat([numid, numindex])
            print(combined)
    else:
        num = int(searchNum)
        numid = df[(df['id'] ==num)]
        numindex = df[df.index==num]
## I have tried everything here to get these to work in one line but i cannot for the life of me get it to work
#I have tried iloc, loc, everything I can think of.         
        combined = pd.concat([numid, numindex])
        print(f"Okay... {num}\n\nHere is the Pokemon with the ID number {num}, as well as the Pokemon at the index {num}\n\n")
        
        print(combined)# -*- coding: utf-8 -*-

