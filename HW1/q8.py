import pandas as pd
import numpy as np



df = pd.read_csv("data/poke.csv")
df2 = pd.read_csv('data/locations.csv')

names = df['identifier']
idNum = df['id']
pokemon_id = df2['pokemon_id']

pokeTeam = []
pokeIndicies = []
pokeLoc = []

pokePlyr = str(input("Enter a Pokemon to start building your team.\n")).lower()


while pokePlyr != "exit":
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
                else:
                    pokePlyr = str(input("List another team member or type 'exit' to stop: \n").lower())  

                     
            
            if pokePlyr == "exit":
                file = open('q8.out', 'w')
                file.write("Your Team: \n")
                for i in pokeTeam:
                    file.write(i +"\n")
                print("Here is your team:\n", pokeTeam)
    else:
        print("Invalid input.")
        pokePlyr = str(input("I meant to say..."))

        


    
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