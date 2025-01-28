import pandas as pd
import numpy as np

## This is incomplete
##didn't have time to make exit from men sel 1



df = pd.read_csv("data/poke.csv")
df2 = pd.read_csv('data/locations.csv')

names = df['identifier']
idNum = df['id']
pokemon_id = df2['pokemon_id']

pokeTeam = []
pokeIndicies = []
pokeLoc = []

menu = int(input("What would you like to do? \n1. Add Pokemon\n2. List team\n3. Drop member\n4. Exit\n\n"))


while menu != 4:
    if menu ==1: 
        pokePlyr = str(input("What pokemon would you like to add?\n")).lower()
        if pokePlyr in df.identifier.values:    
                if len(pokeTeam) < 6:  
                    pokeIndex = df[df['identifier'] == pokePlyr].index[0]
                    pokePlyr = pokePlyr.capitalize() 
                    pokeTeam.append(pokePlyr)
                    pokeIndicies.append(pokeIndex)
                    if len(pokeTeam) == 6:
                        print("Your team is full.")
                        print(pokeTeam)
                        pokePlyr = str(input("New team members will remove your first player. Or, type 'exit' to stop: \n").lower())
                        if pokePlyr != 'exit':
                            pokeTeam.pop(0) 
                            continue
                    elif pokePlyr == 'exit':
                        menu = 4
                        break
                    else:
                        pokePlyr = str(input("List another team member or type 'exit' to stop: \n").lower())  
    
                         
                
                
        else:
            print("Invalid input.")
            pokePlyr = str(input("I meant to say..."))
    
    
    elif menu == 2:
        print("Here's your current team:\n")
        i = 0
        for pokes in pokeTeam:
            i += 1
            print(i, pokes)
            continue
    
    elif menu == 3:
      
            if len(pokeTeam) > 0:
                print("Here is your team.\n ")
                i = 0
                
                for pokes in pokeTeam:
                    i += 1
                    print(i,pokes)
                print("")     
                    
                bye = int(input("What is the number of the pokemon you would like to remove? \n"))-1 
                print("")
                del pokeTeam[bye]
                
                print("Here's your updated list: ")
                i = 0
                for pokes in pokeTeam:
                    i += 1
                    print(i, pokes)
               
                
            else:
                print("Hmm.. seems like you don't have a team yet.")
                print("")
                print("")
        
    elif menu == 4:
        break


    
for i in pokeIndicies:
    loc = (pokemon_id.iloc[i])
    pokeLoc.append(loc)
    
pokeDict = dict(zip(pokeIndicies,pokeLoc))

file = open('q8.out', 'w')
file.write("Your Team: \n")
for i in pokeTeam:
    file.write(i +", ")
file.write("\nTheir Index: \n")
for i in pokeIndicies:
    file.write(str(i) +", ")
file.write("\nTheir Location: \n")
for i in pokeLoc:
    file.write(str(i)+ ", ")
    


file.close()