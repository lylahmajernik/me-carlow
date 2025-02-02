# -*- coding: utf-8 -*-
"""
Q9
Lylah Majernik
HW3
"""

import pandas as pd

df = pd.read_csv("../data/poke.csv")

team = []
loop = True
teamDF = []
print("let's build a team.")


while loop == True:
    menuSel = int(input("What would you like to do?\n1. Add to team\n2. Drop from team\n3. Print team df\n4. Exit\n"))

    if menuSel == 1:
        if len(team)<=5:
            addPoke = str(input("Type the name of the pokemon you'd like to add\n"))
            if addPoke not in df['identifier'].values:
                print("This Pokemon does not exist")
            else:
                team.append(addPoke)
                print("Here is your team:")
                i=0
                for poke in team:
                    i += 1
                    print(i, poke)
                print("")
        elif len(team)==6:
            print("You have reached the max # for your team. Please delete a pokemon to add another.")
    elif menuSel == 2:
       if len(team) > 0:
           print("Here is your team. ")
           print("")
           i = 0
           
           for mem in team:
               i += 1
               print(i,mem)
           print("\n")     
               
           delete = int(input("What is the number of the pokemon you would like to remove? \n"))-1 
           print("")
           team.pop(delete)
           
           print("Here's your updated list: ")
           i = 0
           for mem in team:
               i += 1
               print(i, mem)
           print("")
           
       else:
           print("Hmm.. seems like you don't have anything on your list.")
           print("")
           print("")
    elif menuSel == 3:
        for poke in team:
            if poke in df['identifier'].values:
                  teamData = df[df['identifier'] == poke]
                  teamDF.append(teamData)
        teamDFConcat = pd.concat(teamDF)
        print(teamDFConcat)
    elif menuSel == 4:
        print("Goodbye")
        break
    else:
        print("Invalid input")
        continue
      
        
            
            
            